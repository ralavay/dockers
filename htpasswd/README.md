# htpasswd

Generate simple auth credentials

## Usage

Using htpasswd

```
# Get user:password_hash
htpasswd -nb USER PASSWORD

# Get base64
# Remove the newline from the output of `htpasswd`
htpasswd -nb USER PASSWORD | tr -d '\n' | base64
```

Using Docker

```
docker run --rm ralavay/htpasswd USERNAME PASSSWORD
```

## References

- https://httpd.apache.org/docs/current/programs/htpasswd.html
