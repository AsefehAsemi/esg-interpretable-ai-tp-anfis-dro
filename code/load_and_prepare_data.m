function [X, Y] = load_and_prepare_data()
data = readtable('ANFIS_normalized_dataset.csv');
X = data{:,1:4};
Y = data{:,5};
end
