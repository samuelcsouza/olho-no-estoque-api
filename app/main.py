from config.socketify import app
import routes  # noqa


app.listen(
    3000,
    lambda config: print(f"Listening on port {config.port}")
)

app.run()
