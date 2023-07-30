clc;
clear;
close all;

%% Load Data

data=load('X');
X=data.X;


%% Run DBSCAN Clustering Algorithm

epsilon=0.003;
MinPts=10;
IDX=DBSCAN(X,epsilon,MinPts);


%% Plot Results

PlotClusterinResult(X, IDX);
title(['DBSCAN Clustering (\epsilon = ' num2str(epsilon) ', MinPts = ' num2str(MinPts) ')']);