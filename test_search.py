from src.search import get_live_news_context

print("=" * 50)
print("LIVE SPORTS NEWS")
print("=" * 50)

news = get_live_news_context("Cricket")

print(news)