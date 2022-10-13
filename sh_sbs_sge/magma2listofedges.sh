cat census.mgm | sed -e 's/>;$//g' | sed -e 's/^AT4val//g' | sed -e 's/^\[[0-9]*,[0-9]*\]\ :=\ Graph<[0-9]*\ |\ //g' | sed -e 's/{//g' | sed -e 's/}//g' > census.list 
sed -i '/^$/d' census.list
