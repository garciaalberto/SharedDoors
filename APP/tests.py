from django.test import TestCase
from .models import *
import datetime

class UserTestCase(TestCase):
    def setUp(self):
        flat = Flat.objects.create(name='testFlat', key='1234')
        User.objects.create(name='testUser', allocation=flat, mail='test@mail.com', password='1234', points_monthly=100, points_total=500)

    def test_users_name(self):
        """User got his name correctly added"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.name, 'testUser')

    def test_users_str(self):
        """User returns his name properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.__str__(), 'testUser')

    def test_users_mail(self):
        """User returns his email properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.mail, 'test@mail.com')

    def test_users_password(self):
        """User returns his non-encrypted password properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.password, '1234')

    def test_users_monthly_points(self):
        """User returns his monthly points properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.points_monthly, 100)

    def test_users_total_points(self):
        """User returns his total points properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.points_total, 500)

    def test_users_allocation(self):
        """User returns his allocation properly"""
        user = User.objects.get(name='testUser')
        self.assertEqual(user.allocation.name, 'testFlat')
        self.assertEqual(user.allocation.key, '1234')


class FlatTestCase(TestCase):
    def setUp(self):
        Flat.objects.create(name='testFlat', key='1234')

    def test_flats_name(self):
        """Flat got his name correctly added"""
        flat = Flat.objects.get(name='testFlat')
        self.assertEqual(flat.name, 'testFlat')

    def test_flats_str(self):
        """Flat returns his name properly"""
        flat = Flat.objects.get(name='testFlat')
        self.assertEqual(flat.__str__(), 'testFlat')

    def test_flats_key(self):
        """Flat returns his key properly"""
        flat = Flat.objects.get(name='testFlat')
        self.assertEqual(flat.key, '1234')


class EventTestCase(TestCase):
    def setUp(self):
        flat = Flat.objects.create(name='testFlat', key='1234')
        user = User.objects.create(name='testUser', allocation=flat, mail='test@mail.com', password='1234', points_monthly=100, points_total=500)
        event = Event.objects.create(name='testEvent', day='2018-05-15', allocation=flat, is_completed=True, price=12.4, type='P')
        event.users.add(user)
        event.save()

    def test_events_name(self):
        """Event got his name correctly added"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.name, 'testEvent')

    def test_events_str(self):
        """Event returns his name properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.__str__(), 'testEvent')

    def test_events_day(self):
        """Event returns his date properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.day, datetime.date(2018, 5, 15))

    def test_events_completed(self):
        """Event returns his status properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.is_completed, True)

    def test_events_price(self):
        """Event returns his price properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.price, 12.4)

    def test_events_type(self):
        """Event returns his type properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.type, 'P')

    def test_events_allocation(self):
        """Event returns his allocation properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.allocation.name, 'testFlat')
        self.assertEqual(event.allocation.key, '1234')

    def test_events_users(self):
        """Event returns his user properly"""
        event = Event.objects.get(name='testEvent')
        self.assertEqual(event.users.count(), 1)
        self.assertEqual(event.users.get(name='testUser').name, 'testUser')
        self.assertEqual(event.users.get(name='testUser').mail, 'test@mail.com')
        self.assertEqual(event.users.get(name='testUser').password, '1234')
        self.assertEqual(event.users.get(name='testUser').points_monthly, 100)
        self.assertEqual(event.users.get(name='testUser').points_total, 500)
