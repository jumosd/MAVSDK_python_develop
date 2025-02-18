import asyncio
from mavsdk import System

class Drone:
    def __init__(self):
        self.drone = System()  # MAVSDK 드론 객체 생성

    async def connect(self):
        """드론에 연결하는 함수"""
        await self.drone.connect(system_address="udp://:14550")  # MAVSDK 연결
        print("✅ 드론 연결 성공!")

    async def get_location(self):
        """드론의 실시간 GPS 위치를 가져오는 함수"""
        async for position in self.drone.telemetry.position():
            return position.latitude_deg, position.longitude_deg

    async def get_battery(self):
        """드론의 실시간 배터리 잔량을 가져오는 함수"""
        async for battery in self.drone.telemetry.battery():
            return battery.remaining_percent * 100  # 배터리 잔량 (0~100%)