grep 'Pos' AF_output.txt > temp1.txt
sed -i 's/Position: //'g temp1.txt 
cut -f1 -d ' ' temp1.txt > coors.txt
sed -i 's/:/\t/g' coors.txt 
sed -i 's/Chr/chr/g' coors.txt 
sed -i '/^chrHS/d' coors.txt
rm temp1.txt