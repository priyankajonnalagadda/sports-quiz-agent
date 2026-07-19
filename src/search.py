from ddgs import DDGS


def get_live_news_context(sport_name):
    """
    Retrieve recent sports news using DDGS.
    """

    query = f"{sport_name} latest sports news"

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return "No recent news found."

        news = []

        for i, item in enumerate(results, start=1):
            title = item.get("title", "No Title")
            body = item.get("body", "No Summary")

            news.append(
                f"Source {i}\n"
                f"Title: {title}\n"
                f"Summary: {body}"
            )

        return "\n\n".join(news)

    except Exception as e:
        return f"Search Error: {e}"