#!/bin/bash
echo ""
echo "                                Welcome TO My Scraping                                        "
echo ""
echo "To get required output please read instructions carefully and provide your choices as mentioned or you might get an error."
echo ""
while [ 1 ]
do
  echo "Instru : do you have scrapy installed  ? Y/N"
  echo -n "Choice : "
  read input

  if [ $input == "Y" -o $input == "y" ]
  then
    break
  else
    echo ""
    echo "Make sure you have python install and path set to environment"
    echo ""
    echo "any key to install scrapy"
    echo -n "Choice : "
    read temp
    pip install scrapy
    break
  fi
done
clear
echo ""
echo "                                Welcome TO My Scraping                                        "
echo ""
echo ""
echo "Enter Json File Name to create ( Add .json at last & use charater and '_' only )! Output file will be available in goog directory."
echo ""
echo -n "JSON ( append .json ) name : "
read name
echo ""
echo "Do you have file for Symboles Y/N?"
echo -n "Choice : "
read choice
if [ $choice == "Y" -o $choice == "y" ]
then
  while [ 1 ]
  do
    echo ""
    echo "Make Sure Data In Your File is like, provided in symbol.txt as a sample."
    echo "Enter Absolute File Path from this files position - include ( ./ ) for current directory"
    echo ""
    echo -n "File Path ( With File Extention ) : "
    read file
    if test  -f $file
    then
      break
    else
      echo "Invalide File"
    fi
  done
  clear
  echo ""
  echo "                                Welcome TO My Scraping                                        "
  echo ""
  cd ./goog/
  echo ""
  echo ""
  echo "Processing Gonna Start......"
  echo "Here, I have used Seperate Free-Proxy for each symbol so may take 2-3 min or depend on file you have provided."
  echo "Do you want to continue..Y/N "
  echo ""
  echo -n "Choice : "
  read choice_1
  if [ $choice_1 == "Y" -o $choice_1 == "y" ]
  then
    scrapy crawl GOOGCompetitor -a path=$file -o $name
  else
    echo ""
    echo "Thanks for using..."
  fi
else
  clear
  echo ""
  echo "                                Welcome TO My Scraping                                        "
  echo ""
  echo "Process Going To Start......"
  echo "Here i used Seperate Free-Proxy for each symbol so may take 2-3 min or depend on file you have provided."
  echo "Do you want to continue..Y/N"
  echo -n "Choice : "
  read choice_2
  if [ $choice_2 == "Y" -o $choice_2 == "y" ]
  then
    scrapy crawl GOOGCompetitor -a path=' ' -o $name
  else
    echo ""
  fi
fi
clear
echo ""
echo "                                Welcome TO My Scraping                                        "
echo ""
echo ""
echo "............................Thanks for using......................................"
echo ""
echo "On Success json file will be found in ( goog ) directory. if error then check symbole file formate or .json extention"
echo ""
echo "Press Any Key to Exit"
read any

