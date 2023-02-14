echo "Run migrations"
python manage.py migrate --no-input
echo "Start server"
gunicorn ecotextile.wsgi:application --bind 0.0.0.0:8000