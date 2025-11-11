class EventManager:
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def unregister_listener(self, listener):
        self.listeners.remove(listener)

class Component:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self.on_event)

    def on_event(self, event):
        print(f"Component received event: {event}")

    def __del__(self):
        self.event_manager.unregister_listener(self.on_event)


event_mgr = EventManager()
components = []

for i in range(1000):
    comp = Component(event_mgr)
    components.append(comp)

# Even if we delete components, they remain in event_mgr.listeners
del components
