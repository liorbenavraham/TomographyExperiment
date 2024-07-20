% Insert Video Name Below
v = VideoReader('partA_50.mp4');

% Get the number of frames in the video
numFrames = v.NumFrames; 

% Rows to run before to locate the coordinates of the camera feed
%pcolor(frame(:,:,1))
%shading flat

% Main sum loop
for i = 1:numFrames
    frame = read(v, i);

    % Instructions = sum(sum(frame(lower_leftY:upper_rightY,lower_leftX:upper_rightX,1)))

    %%%%%Alice V
    VA(i)=sum(sum(frame(418:666,911:1244,1)));

    %%%%%Bob V
    %VB(i)=sum(sum(frame(419:666,478:809,1)));

    %%%%%Alice H
    %HA(i)=sum(sum(frame(66:313,907:1238,1)));

    %%%%%Bob H
    %HB(i)=sum(sum(frame(200:250,610:670,1)));
    %%%%%

end

figure;
plot(VA);
xlabel('Frame');
ylabel('Sum of Pixels');
title('Intensity of Frame');
