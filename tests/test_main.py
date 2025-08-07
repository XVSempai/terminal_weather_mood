from terminal_weather_mood.main import mood_for

def test_mood_for():
    assert "smile" in mood_for("Sunny")
    assert "reflection" in mood_for("Cloudy")
    assert "decide" in mood_for("Alien Weather")
