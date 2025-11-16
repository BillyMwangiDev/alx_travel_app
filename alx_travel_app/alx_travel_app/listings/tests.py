from django.test import TestCase
from django.core.management import call_command
from django.db import IntegrityError
from datetime import date
from decimal import Decimal

from .models import Listing, Booking, Review
from .serializers import BookingSerializer, ListingSerializer


class ListingModelTest(TestCase):
    def test_create_listing(self):
        listing = Listing.objects.create(
            title="Test Listing",
            description="Nice place",
            location="Test City",
            price_per_night=Decimal("100.00"),
            max_guests=3,
        )
        self.assertIsNotNone(listing.id)
        self.assertEqual(listing.max_guests, 3)


class BookingModelConstraintTest(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            title="L1",
            description="D",
            location="Loc",
            price_per_night=Decimal("50.00"),
            max_guests=2,
        )

    def test_end_date_after_start_constraint(self):
        serializer = BookingSerializer(
            data={
                "listing": self.listing.id,
                "guest_name": "John",
                "guest_email": "john@example.com",
                "start_date": date(2025, 1, 10),
                "end_date": date(2025, 1, 12),
                "total_price": "100.00",
                "status": "PENDING",
            }
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        booking = serializer.save()
        self.assertIsNotNone(booking.id)

        bad = BookingSerializer(
            data={
                "listing": self.listing.id,
                "guest_name": "Bad",
                "guest_email": "bad@example.com",
                "start_date": date(2025, 1, 10),
                "end_date": date(2025, 1, 9),
                "total_price": "50.00",
                "status": "PENDING",
            }
        )
        self.assertFalse(bad.is_valid())


class SeedCommandTest(TestCase):
    def test_seed_creates_data(self):
        call_command("seed", listings=2, bookings_per_listing=1, reviews_per_listing=1, flush=True)
        self.assertEqual(Listing.objects.count(), 2)
        self.assertEqual(Booking.objects.count(), 2)  # one per listing
        self.assertEqual(Review.objects.count(), 2)   # one per listing
