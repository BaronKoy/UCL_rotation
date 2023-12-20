awk '{print $2}' HGDP_variants.txt > positions.txt
#Replace with desired chromosome & gene
for x in *_chr$!_selection.sele ; do awk '{print $1,$2,$35}' "$x" | grep -wf ../../$!/positions.txt > ../../$!/pop_data/"$x"_p_values.txt ; done
for x in *.txt ; do awk ' $3 > -0.05 ' "$x" > significance/"$x".sig.txt ; done
for x in *.txt ; do awk ' $3 < 0.05 ' "$x" > final/"$x".sig.txt ; done