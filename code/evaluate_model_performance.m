function evaluate_model_performance(fis, X, Y)
Y_pred = evalfis(fis, X);
rmse = sqrt(mean((Y - Y_pred).^2));
fprintf('ANFIS RMSE: %.4f\n', rmse);
end
