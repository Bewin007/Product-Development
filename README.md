# Product-Development
>In this human body is detected with the help of the [mediapipe]
Then we use some mathematical functions to calculate how much the excercise is done.

## Sit-Up Exercise

The sit-up is an abdominal endurance training exercise to strengthen, tighten and tone the abdominal muscles. It is similar to a crunch, but sit-ups have a fuller range of motion and condition additional muscles.
```
python main.py -t sit-up -vs videos/sit-up.mp4
```


## Pull-Up Exercise

A pull-up is an upper-body strength exercise. The pull-up is a closed-chain movement where the body is suspended by the hands and pulls up. As this happens, the elbows flex and the shoulders adduct and extend to bring the elbows to the torso.
```
python main.py -t pull-up -vs videos/pull-up.mp4
```


## Squat Exercise

A squat is a strength exercise in which the trainee lowers their hips from a standing position and then stands back up. During the descent of a squat, the hip and knee joints flex while the ankle joint dorsiflexes; conversely the hip and knee joints extend and the ankle joint plantarflexes when standing up.
```
python main.py -t squat -vs videos/squat.mp4
```


## Walking Exercise

```
python main.py -t walk -vs videos/walk.mp4
```

---

Note: It needs to be in the Product Development folder before running the code.
      You can use 'cd' for navigation between folders in Windows and Linux.

You can also detect your movements live with your webcam, you can run the code in the below line to use this in GUI.
```
python qna.py
```

If you need to run a particular exercise you can use the below code.

Sit up
```
python main.py -t sit-up
```
Pull up
```
python main.py -t pull-up
```
Push up
```
python main.py -t push-up
```
Squat
```
python main.py -t squat
```
Walk
```
python main.py -t walk
```
