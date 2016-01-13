# catalog-postgres-ubuntu

Catalog project adapted to utilize Postgres and run off an Ubuntu server. Public IP and Host Name are not permanent and will expire. Instructions can be easily adapted to run off a VM.

1. Public IP: [52.11.60.186](http://52.11.60.186)
2. Host Name: [ec2-52-11-60-186.us-west-2.compute.amazonaws.com](http://ec2-52-11-60-186.us-west-2.compute.amazonaws.com)
2. SSH port: 2200
3. Additional Resources:
	* [SSHD Configuration](http://linux.die.net/man/5/sshd_config)
	* [.htaccess files](https://httpd.apache.org/docs/2.4/howto/htaccess.html)
	* [Troubleshooting psycopg2 installation](http://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python)
	* [Running Apache with virtualenv](http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/)
	* [Udacity project discussion thread](https://discussions.udacity.com/t/p5-how-i-got-through-it/15342/19)
	* [Monitor logins using fail2ban](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-14-04)
4. Ubuntu packages
	* ntp
	* apache2
	* libapache2-mod-wsgi
	* git
	* python-pip
	* python-dev
	* postgresql
	* postgresql-contrib
	* libpq-dev
	* python-psycopg2

---
# Installation

### 1. Launch AWS machine

* Download `udacity_key.rsa` from [Udacity](https://www.udacity.com/account#!/development_environment).

```
$ mv ~/Downloads/udacity_key.rsa ~/.ssh/
$ chmod 600 ~/.ssh/udacity_key.rsa
$ ssh -i ~/.ssh/udacity_key.rsa root@52.34.141.227
```

### 2. Create new user and give sudo permissions

```
$ adduser USERNAME
$ echo "USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/USERNAME
```

### 3. Update all currently installed packages

```
$ sudo apt-get update && sudo apt-get upgrade
```

### 4. Configure local timezone to UTC

```
$ echo "Etc/UTC" | sudo tee /etc/timezone
$ sudo dpkg-reconfigure --frontend noninteractive tzdata
```

### 5. (Recommended) Sync server time automatically with NTP

```
$ sudo apt-get install ntp
```

* Update via ntpd: Choose a local server pool from [NTP Pool Project](http://www.pool.ntp.org/en/) and add to `/etc/ntp.conf`.


### 6. Reconfigure SSH

```
$ vi /etc/ssh/sshd_config
```

* Change values

	1. `Port 2200`
	2. `PermitRootLogin no`
	3. `PasswordAuthentication yes` (temporary until firewall is setup)

* Append values
	1. `UseDNS no`
	2. `AllowUsers USERNAME`

* Restart SSH service

	```
$ service ssh restart
```


### 7. Use SSH key for login and disable PW-based auth

```
# Switch to local machine and create a new public key
# Save file as `grader_rsa`. Passphrase is optional.
$ ssh-keygen

# Copy public key to server
$ cat path/to/grader_rsa.pub | ssh USERNAME@REMOTE_SERVER -pSSH_PORT "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Test login
$ ssh -i path/to/grader_rsa.pub USERNAME@REMOTE_SERVER -pSSH_PORT

$ sudo vi /etc/ssh/sshd_config
```

* Change value

	1. `PasswordAuthentication no`  


### 8. Configure firewall

```
$ sudo ufw default allow outgoing
$ sudo ufw default deny incoming

# Allow SSH, HTTP, and NTP
$ sudo ufw allow 2200
$ sudo ufw allow 80
$ sudo ufw allow 123

# (Optional) Double-check rules
$ cat /lib/ufw/user*.rules

# Turn on firewall
$ sudo ufw enable
$ sudo ufw status verbose

```

### 9. Setup Apache to serve app

```
$ sudo apt-get install apache2 libapache2-mod-wsgi
$ sudo service apache2 restart
```

### 10. Setup Catalog project


1. Setup git to clone project

	```
$ sudo apt-get install git
$ git config --global user.name "YOUR NAME"
$ git config --global user.email "YOUR EMAIL"
```
2. Prepare project folder

	```
$ sudo mkdir /var/www/catalog && cd /var/www/catalog
```
3. Clone GH repo and make web-inaccessible

	```
$ cd /var/www/
$ sudo git clone https://github.com/jrrembert/catalog-postgres-ubuntu.git
$ sudo cp -R catalog-postgres-ubuntu/* catalog/
$ echo "RedirectMatch 404 /\.git" | sudo tee catalog/.htaccess
```
4. Setup project dependencies

	```
$ sudo apt-get install python-pip python-dev
```
5. Setup virtualenv

	```
$ sudo pip install virtualenv
$ virtualenv /var/www/catalog/venv
$ sudo chmod -R 777 /var/www/catalog/venv # a bit brutish, could be improved
$ source /var/www/catalog/venv/bin/activate
```

### 11. Configure Virtual Host and WSGI files

1. Open new VH file

	```
$ sudo vi /etc/apache2/sites-available/catalog.conf
```
* Enter the following, changing values as needed

	```
<VirtualHost *:80>
      ServerName PUBLIC-IP-ADDRESS
      ServerAlias HOSTNAME
      ServerAdmin admin@PUBLIC-IP-ADDRESS
      WSGIScriptAlias / /var/www/catalog/catalog.wsgi
      <Directory /var/www/catalog/catalog_project/>
          Order allow,deny
          Allow from all
      </Directory>
      Alias /static /var/www/catalog/catalog_project/static
      <Directory /var/www/catalog/catalog_project/static/>
          Order allow,deny
          Allow from all
      </Directory>
      ErrorLog ${APACHE_LOG_DIR}/error.log
      LogLevel warn
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
```

3. Create .wsgi file

	```
$ sudo vi /var/www/catalog/catalog.wsgi
```

4. Enter the following, changing values as needed

	```
	#!/usr/bin/python
	import os
	import logging
	import site
	import sys
	
	logging.basicConfig(stream=sys.stderr)
	sys.path.insert(0,"/var/www/catalog/")
	sys.path.append("/var/www/catalog/catalog_project")
	
	site.addsitedir("/var/www/catalog/venv/local/lib/python2.7/site-packages")
	activate_env=os.path.abspath("/var/www/catalog/venv/bin/activate_this.py")
	execfile(activate_env, dict(__file__=activate_env))
	
	from catalog_project import app as application
	
	application.secret_key = 'Add your client secret from client_secrets.json' 
	```
  
3. Enable Virtual Hosts file and restart

	```
$ sudo a2ensite catalog
$ sudo service apache2 restart
```



### 12. Install and configure PostgreSQL

1. Install Postgres and extensions

	```
	$ sudo apt-get install postgresql postgresql-contrib libpq-dev python-psycopg2

	# Check and make sure remote connections are disabled
	$ sudo cat /etc/postgresql/9.3/main/pg_hba.conf
```

2. Set the following values in `config.py`.

	```
DATABASE_CONNECT_OPTIONS = {
    'PG_DB_NAME': 'catalog',
    'PG_USERNAME' : 'catalog',
    'PG_PASSWORD': 'catalog',
    'PG_HOST': 'localhost',
}
```

3. Config Postgres (substitute values from `config.py` where appropriate)

	```
	$ sudo adduser "PG_USERNAME"
	$ sudo su - postgres
	$ psql

	Enter the following:

	# CREATE USER PG_USERNAME WITH PASSWORD 'PG_PASSWORD'; # Make sure password is enclosed by single quotes!
	# ALTER USER PG_USERNAME CREATEDB;
	# CREATE DATABASE PG_DB_NAME WITH OWNER PG_USERNAME;
	# \c PG_DB_NAME
	# REVOKE ALL ON SCHEMA public FROM public;
	# GRANT ALL ON SCHEMA public TO PG_USERNAME;
	# \q
	
	$ exit
```

4. Import db schema

	```
	$ cd /var/www/catalog
	$ python -c "import database; database.init_db()"

	# Install remaining project dependencies (make sure you have a virtualenv activated)
	$ pip install -r requirements-ubuntu.txt
	$ sudo service apache2 restart
```


5. Check that application works by opening a browser and entering public IP.



### 13. Setup Google Oauth

1. Go to https://console.developers.google.com and update your javascript origins and redirect URIs
2. Download your updated client secret file and save it to `/var/www/catalog/client_secrets.json`
3. Restart Apache server if necessary.
4. Test site by going to hostname url (not public ip url).


# Optional

### 1. Set server to periodically update installed packages

```
$ sudo apt-get install unattended-upgrades
```

* Upgrades can cause critical app components to break unexpectedly so we will configure unattended-upgrades to update security patches only.

	1. Open `/etc/apt/apt.conf.d/50unattended-upgrades`.
	2. Verify that `"${distro_id}:${distro_codename}-security";` is uncommented and other options under `Unattended-Upgrade::Allowed-Origins` are.
	
### 2. Setup Fail2Ban to monitor unsuccessful login attempts.

1. Initial installation

	```
$ sudo apt-get install fail2ban sendmail
$ sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
$ sudo vi /etc/fail2ban/jail.local
```

2. Change the following:
	
	```
maxretry = 10
destemail = ADMIN_EMAIL
action = %(action_mwl)s
port = SSH PORT
```
	
3. Restart fail2ban

	```
$ sudo service fail2ban stop
$ sudo service fail2ban start
```

### 3. System monitoring

```
$ sudo apt-get install htop
$ htop
``` 






















