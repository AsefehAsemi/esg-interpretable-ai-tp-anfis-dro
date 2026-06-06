% Main ANFIS pipeline as described in the manuscript
clear; clc;

[X, Y] = load_and_prepare_data();
mf = define_membership_functions();
fis = build_initial_fis(mf);
trained_fis = train_anfis_model(fis, X, Y);
extract_fuzzy_rules(trained_fis);
evaluate_model_performance(trained_fis, X, Y);

writefis(trained_fis, 'esg_fixed.fis');
