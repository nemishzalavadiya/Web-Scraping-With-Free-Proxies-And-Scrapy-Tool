#!/bin/bash
echo "Welcome TO My Scraping"
echo ""
echo "Enter Json File Name to create ( Add .json at last )?"
read name
echo "Do you have file for Symboles Y/N?"
read choice
if [ $choice == "Y" ]
then
  while [ 1 ]
  do
    echo "Enter Absolute File Path for current directory include ( ./ )"
    read file
    if test  -f $file
    then
      break
    else
      echo "Invalide File"
    fi
  done

  cd ./goog/
  echo ""
  echo ""
  echo "nProcessing Gonna Start......"
  echo "Here, I have used Seperate Proxy for each symbol so may take 2-3 min "
  echo "Do you want to continue..Y/N "
  echo ""
  echo ""
  read choice_1
  if [ $choice_1 == "Y" ]
  then
    scrapy crawl GOOGCompetitor -a path=$file -o $name
  else
    echo ""
    echo "Thanks for using..."
  fi
else
  echo ""
  echo "Process Going To Start......"
  echo "Here i used Seperate Proxy for each symbol so may take 2-3 min -"
  echo "Do you want to continue..Y/N"
  read choice_2
  if [ $choice_2 == "Y" ]
  then
    scrapy crawl GOOGCompetitor -a path=' ' -o $name
  else
    echo ""
    echo "Thanks for using..."
  fi
fi
echo ""
echo "json file will found in ( goog ) directory ...."
echo ""
echo "Press Any Key to Exit"
read any

