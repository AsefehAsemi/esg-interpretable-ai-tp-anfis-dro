function trained_fis = train_anfis_model(fis, X, Y)
data = [X Y];
options = anfisOptions;
options.InitialFIS = fis;
options.EpochNumber = 2;
trained_fis = anfis(data, options);
end
