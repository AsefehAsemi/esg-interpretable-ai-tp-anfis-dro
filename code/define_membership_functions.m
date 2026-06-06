function mf = define_membership_functions()
mf.labels = {'VeryLow','Low','Medium','High','VeryHigh'};
mf.type = 'trimf';
mf.range = [0 1];
mf.params = [
    0.0 0.0 0.25;
    0.0 0.25 0.5;
    0.25 0.5 0.75;
    0.5 0.75 1.0;
    0.75 1.0 1.0
];
end
