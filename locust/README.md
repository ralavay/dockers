# locust.io

## Usage

Run with docker

```
docker run --rm -i -v $PWD:/tmp ralavay/locust sh -c "locust --no-web -c 1 -r 1 -t 10s --only-summary -f /tmp/test.py"
```

## References

- https://locust.io/
