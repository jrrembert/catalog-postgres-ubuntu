function setup {
	if [ -d /vagrant ]; then
		cd /vagrant
		if [ -e ./catalog_project/app.db ]; then
			rm ./catalog_project/app.db
		fi
		python -c "import database; database.init_db()"
		echo "Database created."
		python teamdata.py
	fi

	exit
}

echo "This is to be run from within the provided VM." 
echo "Running outside the VM could have unintended effects."

while true; do
	read -p "Do you wish to run this script (y or n)? " yn
	case $yn in
		[Yy]* ) setup;;
		[Nn]* ) exit;;
		* ) echo "Please answer yes or no.";;
	esac
done
