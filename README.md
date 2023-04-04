# Cern_beamline
For camera streaming
  - raspivid -o - -t 0 -vf -w 800 -h 400 -n -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264 (command)



Temperature sensor - shorturl.at/bisw7 or  shorturl.at/gwEHZ

Imu sensor https://www.adafruit.com/product/3463
  
