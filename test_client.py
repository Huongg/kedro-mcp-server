import asyncio
from weather import get_alerts, get_forecast

async def main():
    # Test get_alerts
    print("Fetching alerts for Texas...")
    alerts = await get_alerts("TX")
    print(alerts)

    # Test get_forecast
    print("Fetching forecast for Texas...")
    forecast = await get_forecast(31.9686, -99.9018)  # Latitude and longitude for Texas
    print(forecast)

if __name__ == "__main__":
    asyncio.run(main())