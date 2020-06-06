#!/bin/bash
echo "Welcome TO My Scraping"
while [ 1 ]
do
  echo "do you have scrapy installed  ? Y/N"
  read input
  if [ $read =="Y" or $read == "y" ]
  then
    break
  else
    echo "Make sure you have python install and path set to environment"
    echo "any key to install scrapy"
    read temp
    pip install scrapy
    break
done
echo ""
echo "Enter Json File Name to create ( Add .json at last )! file will be available in goog directory."
read name
echo "Do you have file for Symboles Y/N?"
read choice
if [ $choice == "Y" or $choice == "y" ]
then
  while [ 1 ]
  do
    echo "Make Sure Data In Your File is like, provided in symbol.txt as a sample."
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
  echo "Processing Gonna Start......"
  echo "Here, I have used Seperate Proxy for each symbol so may take 2-3 min or depend on file you have provided."
  echo "Do you want to continue..Y/N "
  echo ""
  echo ""
  read choice_1
  if [ $choice_1 == "Y" or $choice_1 == "y" ]
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
  if [ $choice_2 == "Y" or $choice_2 == "y" ]
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

