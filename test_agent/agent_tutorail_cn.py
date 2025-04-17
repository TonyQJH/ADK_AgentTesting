## 🔥天气预报
import datetime
import requests
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.agents import LlmAgent

from google.adk.models.lite_llm import LiteLlm

# 城市名称映射字典，将中文城市名映射到英文
CITY_NAME_MAP = {
    "纽约": "New York",
    "伦敦": "London",
    "东京": "Tokyo",
    "北京": "Beijing",
    "上海": "Shanghai",
    "巴黎": "Paris",
    "柏林": "Berlin",
    "悉尼": "Sydney",
    "莫斯科": "Moscow",
    "迪拜": "Dubai",
    # 可以继续添加更多常用城市
}

def get_weather(city: str) -> dict:
    """获取指定城市的当前天气报告。

    使用weatherapi.com的API获取实时天气数据。
    支持中文城市名，内部会自动转换为英文名。

    参数:
        city (str): 要获取天气报告的城市名称（中文或英文）。

    返回:
        dict: 包含状态和结果或错误信息的字典。
    """
    # API密钥和基础URL
    api_key = "7dd6adfdddfb4309ab7132443240409"
    base_url = "http://api.weatherapi.com/v1/current.json"

    # 检查城市名是否需要转换为英文
    query_city = CITY_NAME_MAP.get(city, city)

    try:
        # 构建API请求
        params = {
            "key": api_key,
            "q": query_city
        }

        # 发送GET请求到天气API
        response = requests.get(base_url, params=params)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析JSON响应
            data = response.json()

            # 提取相关天气信息
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            temp_f = data["current"]["temp_f"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]

            # 构建天气报告（使用原始输入的城市名）
            report = (
                f"当前{city}({country})的天气为{condition}，"
                f"温度{temp_c}°C ({temp_f}°F)，"
                f"湿度{humidity}%，风速{wind_kph}公里/小时。"
            )

            return {
                "status": "success",
                "report": report,
            }
        else:
            # 处理API错误
            return {
                "status": "error",
                "error_message": f"无法获取'{city}'的天气信息。API响应代码: {response.status_code}，请检查城市名称是否正确。"
            }
    except Exception as e:
        # 处理其他异常
        return {
            "status": "error",
            "error_message": f"获取'{city}'的天气信息时出错: {str(e)}"
        }
def intro() -> dict:
    return {
        "status": "success",
        "report": "I can answer your questions about the time and weather in a city."
    }

def get_current_time(city: str) -> dict:
    """获取指定城市的当前时间。

    使用weatherapi.com的API获取城市的时区信息，
    然后根据时区计算当前时间。
    支持中文城市名，内部会自动转换为英文名。

    参数:
        city (str): 要获取当前时间的城市名称（中文或英文）。

    返回:
        dict: 包含状态和结果或错误信息的字典。
    """
    # API密钥和基础URL（与天气API相同）
    api_key = "7dd6adfdddfb4309ab7132443240409"
    base_url = "http://api.weatherapi.com/v1/current.json"

    # 检查城市名是否需要转换为英文
    query_city = CITY_NAME_MAP.get(city, city)

    try:
        # 构建API请求
        params = {
            "key": api_key,
            "q": query_city
        }

        # 发送GET请求到API获取时区信息
        response = requests.get(base_url, params=params)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析JSON响应
            data = response.json()

            # 提取时区ID和本地时间
            tz_id = data["location"]["tz_id"]
            localtime = data["location"]["localtime"]

            # 构建时间报告（使用原始输入的城市名）
            report = f"当前{city}的时间是 {localtime} ({tz_id}时区)"

            return {
                "status": "success",
                "report": report
            }
        else:
            # 处理API错误
            return {
                "status": "error",
                "error_message": f"无法获取'{city}'的时区信息。API响应代码: {response.status_code}，请检查城市名称是否正确。"
            }
    except Exception as e:
        # 处理其他异常
        return {
            "status": "error",
            "error_message": f"获取'{city}'的时间信息时出错: {str(e)}"
        }

# 创建根代理
root_agent = Agent(
    name="weather_time_agent",  # 代理名称
    model=LiteLlm(model="ollama_chat/llama3.2:3b"),
    description=(
        "智能助手，可以回答关于各个城市的天气和时间问题。"
    ),  # 代理描述
    instruction=(
        "我是一个能够提供城市天气和时间信息的智能助手。"
        "当用户询问某个城市的天气情况时，使用get_weather工具获取最新天气数据。"
        "当用户询问某个城市的当前时间时，使用get_current_time工具获取准确时间。"
        "当用户询问这个agent可以做什么的时候，使用intro工具获取准确时间。"
        "请以友好的方式回应用户的询问，并提供完整的天气或时间信息。"
        "我能够理解中文城市名称，并自动转换为对应的英文名。"
    ),  # 代理指令（中文版）
    tools=[get_weather, get_current_time, intro],  # 可用工具
)

