from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import feed.routing

application = ProtocolTypeRouter({
	'websocket' : AuthMiddlewareStack(
		URLRouter(
			feed.routing.websocket_urlpatterns)),
	})