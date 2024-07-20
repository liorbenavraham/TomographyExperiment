clear all

filename='HHVV10';
base=filename(1:4)
bit_num=filename(5:6)

% Set title
title_figure=strcat(base,{' '},num2str(bit_num),{' '},'bits')

% Read matrix
data=readmatrix(strcat(filename,'.csv'))
bit_num = str2double(bit_num);
data = data / bit_num;  


% AXIS TITLES
Li=["VV","VH","HV","HH"];
Ls=["HH","HV","VH","VV"];


% PLOT
fig=figure;
%G2_plot=bar3(data(1:4,1:4)/sum(sum(data(1:4,1:4))));
G2_plot=bar3(data(1:4,1:4));

for k = 1:length(G2_plot)
    zdata = G2_plot(k).ZData;
    G2_plot(k).CData = zdata;
    G2_plot(k).FaceColor = 'interp';
end

% Set axis labels
titles_size=25;
set(gca,'FontWeight','bold')
set(gca,'FontName','Times New Roman')
set(gca,'Fontsize',15)
set(gca,'XTickLabel',((Li)));
set(gca,'YTickLabel',((Ls)));

title(title_figure,'FontName','Times New Roman','FontSize',titles_size);
colormap default;

% Calculate Z axis
high_array=max(data);
high_num=max(high_array);
set(gca,'Ztick',round([0:(high_num/5):high_num],2));

% Save the fig file
savefig(filename);

% Save the figure as PNG image too
filename = strcat(filename, '.png');
saveas(fig, filename, 'png');
