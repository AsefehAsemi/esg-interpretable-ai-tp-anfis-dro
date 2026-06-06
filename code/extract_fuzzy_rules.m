function extract_fuzzy_rules(fis)
rules = fis.Rules;
fid = fopen('optimized_anfis_rules.txt','w');
for i = 1:length(rules)
    fprintf(fid, '%s\n', rules(i).Description);
end
fclose(fid);
end
