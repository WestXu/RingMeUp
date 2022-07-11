# RingMeUp

Send an alarm to your iPhone to ring you up from a failed script when you are asleep.

## Install

`git clone https://github.com/WestXu/RingMeUp && pip install ./RingMeUp/`

because [#1](https://github.com/WestXu/RingMeUp/issues/1) unfortunately. 

## Usage

Set env variables of `icloud_id`,  `icloud_password` and `device_name`. If your icloud account is in China, also set `icloud_china=1`.

Then:

```
ring
```

Or

```
ring serve [port]
```

to start a server accepting `get`s to ring.

## Docker

```
docker run --rm -e icloud_id=**** -e icloud_password=**** device_name=**** westxu/ring-me-up
```

Or

```
docker run -d --name ring -e icloud_id=**** -e icloud_password=**** device_name=**** -p 11180:80 ring-me-up serve
```
