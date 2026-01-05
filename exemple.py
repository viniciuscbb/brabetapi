from brabetapi.api import BrabetAPI

API = BrabetAPI()


double_history = API.get_double_history()
print(double_history)

formatted_history = API.format_double_history(double_history)
print(formatted_history)

crash_history = API.get_crash_history()
print(crash_history)