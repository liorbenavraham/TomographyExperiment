% Insert Video Name Below
v = VideoReader("a0b225.mp4");

% Get the number of frames in the video
numFrames = v.NumFrames;

% Rows to run before to locate the coordinates of the camera feed
%pcolor(frame(:,:,1))
%shading flat

% Main sum loop
for i = 1:numFrames
    frame = read(v, i);


    % Instructions = sum(sum(frame(lower_leftY:upper_rightY,lower_leftX:upper_rightX,1)))

    %%%%% Alice
    A(i)=sum(sum(frame(224:315,608:730,1)));

    %%%%% Bob
    B(i)=sum(sum(frame(307:398,1030:1146,1)));

end

figure;
plot(A);
hold on
plot(B);

xlabel('Frame');
ylabel('Sum of Pixels');
title('Intensity of Frame');
