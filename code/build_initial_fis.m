function fis = build_initial_fis(mf)
fis = sugfis('Name','ESG_ANFIS_Model');
inputNames = {'Environmental','Governance','Profit','Carbon'};
for i = 1:4
    fis = addInput(fis, mf.range, 'Name', inputNames{i});
    for j = 1:length(mf.labels)
        fis = addMF(fis, inputNames{i}, mf.type, mf.labels{j}, mf.params(j,:));
    end
end
fis = addOutput(fis, [1 3], 'Name', 'InvestorType');
fis = addMF(fis, 'InvestorType', 'constant', 'out1', 1);
end
