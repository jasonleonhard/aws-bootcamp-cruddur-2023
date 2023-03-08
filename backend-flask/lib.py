from datetime import datetime, timedelta, timezone


def now():
    now = datetime.now(timezone.utc).astimezone()
    return now.isoformat()


def created_at(days):
    now = datetime.now(timezone.utc).astimezone()
    return (now - timedelta(days=days)).isoformat()


def expires_at(days):
    now = datetime.now(timezone.utc).astimezone()
    return (now + timedelta(days=days)).isoformat()


def created_at_hours(hours):
    now = datetime.now(timezone.utc).astimezone()
    return (now - timedelta(hours=hours)).isoformat()


def expires_at_hours(hours):
    now = datetime.now(timezone.utc).astimezone()
    return (now + timedelta(hours=hours)).isoformat()
