# RingMeUp

Send an alarm to your iPhone to ring you up from a failed script when you are asleep.

## Install

`pip install ring-me-up`

## Usage

Set env variables of `icloud_id` & `icloud_password`.

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
docker run --rm -e icloud_id=**** -e icloud_password=**** westxu/ring-me-up
```

Or

```
docker run -d --name ring -e icloud_id=**** -e icloud_password=**** -p 11180:80 ring-me-up serve
```
