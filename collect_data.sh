#!/bin/bash

doyear () {
echo "${!1}"
rm data/"${!1}".csv
cat ~/Downloads/leagues*"${!1}"*games.csv >> data/"${!1}".csv
cat ~/Downloads/leagues*"${!1}"*playoffs.csv >> data/"${!1}".csv
sed -i 's/,,Box/,Box/' data/"${!1}".csv
sed -i '/October,October,October,October,October,October,October,October,October/d' data/"${!1}".csv
sed -i '/November,November,November,November,November,November,November,November,November/d' data/"${!1}".csv
sed -i '/December,December,December,December,December,December,December,December,December/d' data/"${!1}".csv
sed -i '/January,January,January,January,January,January,January,January,January/d' data/"${!1}".csv
sed -i '/February,February,February,February,February,February,February,February,February/d' data/"${!1}".csv
sed -i '/March,March,March,March,March,March,March,March,March/d' data/"${!1}".csv
sed -i '/April,April,April,April,April,April,April,April,April/d' data/"${!1}".csv
sed -i '/May,May,May,May,May,May,May,May,May/d' data/"${!1}".csv
sed -i '/June,June,June,June,June,June,June,June,June/d' data/"${!1}".csv
sed -i '/Date,Start (ET),,Visitor\/Neutral,PTS,Home\/Neutral,PTS,,Notes/d' data/"${!1}".csv
sed -i '/Date,,Visitor\/Neutral,PTSv,Home\/Neutral,PTSh,,Notes/d' data/"${!1}".csv
sed -i 's/,.*:.*,Box/,Box/' data/"${!1}".csv
}

start=1947
end=2017
YEAR=$start
while [ $YEAR -lt $end ]; do
    doyear YEAR
    let YEAR+=1
done
