from django.db import migrations
from django.contrib.auth.models import User

def seed(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')
    Bid = apps.get_model('auction', 'Bid')
    Comments = apps.get_model('auction', 'Comments')
    Donation = apps.get_model('auction', 'Donation')

    user1 = User(username='pikachu', password='testing1234', email='p@p.com', first_name='pikachu', last_name='mice')
    user1.save()
    user2 = User(username='jerry', password='testing1234', email='j@j.com', first_name='Jerry', last_name='mice')
    user2.save()
    user3 = User(username='teemo', password='testing1234', email='t@t.com', first_name='Teemo', last_name='mice')
    user3.save()
    user4 = User(username='spiderman', password='testing1234', email='s@s.com', first_name='Peter', last_name='Parker')
    user4.save()

    profile_one = Profile(user_id=user1.id, bio="Pikachu (Japanese: ピカチュウ Hepburn: Pikachū, pronounced [pikatɕɯː], English: /ˈpiːkətʃuː/) are a species of Pokémon, fictional creatures that appear in an assortment of video games, animated television shows and movies, trading card games, and comic books licensed by The Pokémon Company, a Japanese corporation. They are yellow rodent-like creatures with powerful electrical abilities. In most vocalized appearances, including the anime and certain video games, they are primarily voiced by Ikue Ōtani. A Pikachu also appears as part of the main cast in the live-action animated film Pokémon Detective Pikachu, played in CGI and voiced by Ryan Reynolds.", picture='https://i.ytimg.com/vi/1roy4o4tqQM/maxresdefault.jpg')
    profile_two = Profile(user_id=user2.id, bio="Jerry Mouse is a fictional character and one of the title characters (the other being Tom Cat) in Metro-Goldwyn-Mayer's series of Tom and Jerry theatrical cartoon short films. Created by William Hanna and Joseph Barbera, Jerry is a brown anthropomorphic house mouse, who first appeared as a mouse named Jinx in the 1940 MGM animated short Puss Gets the Boot.[1] Hanna gave the mouse's original name as 'Jinx',[2] while Barbera claimed the mouse went unnamed in his first appearance.", picture='https://i.kym-cdn.com/photos/images/original/001/025/640/6da.png')
    profile_three = Profile(user_id=user3.id, bio="Created and rated by players, search through some of the best builds to increase your game and dominate the field of battle. Players guide you through every step of Teemo creation, modification and play style. League of Legends guides are sorted by how up to date they are, but can ...", picture='http://pm1.narvii.com/6919/8beca77c10bb36006feea5fb564722621025048dr1-500-393v2_uhq.jpg')
    profile_four = Profile(user_id=user4.id, bio='The fictional character Spider-Man, a comic book superhero created by Stan Lee and Steve Ditko and featured in Marvel Comics publications, has currently appeared in ten live-action films since his inception, not including fan made shorts and guest appearances in other Marvel Cinematic Universe (MCU) films.', picture='https://images-na.ssl-images-amazon.com/images/I/61r8JEd%2BYhL._SY606_.jpg')

    profile_one.save()
    profile_two.save()
    profile_three.save()
    profile_four.save()

    bid_one = Bid(
    profile = profile_one,
    name = "Ticket to Las Vegas",
    start_date = "2019-04-13T20:00Z",
    end_date = "2019-08-15T20:00Z",
    start_amount = "1000",
    description = "A Plane Ticket to Las Vegas for 2 days one night and hang out with Lebron James!",
    picture = "http://cdn.cnn.com/cnnnext/dam/assets/180313182911-01-las-vegas-travel-strip-super-tease.jpg"
    )
    bid_two = Bid(
    profile = profile_two,
    name = "Ticket to Miami",
    start_date = "2019-01-21T03:00Z",
    end_date = "2019-11-24T04:30Z",
    start_amount = "1500",
    description = "3 Days 2 Night to Miami and meet Justin Bieber. Hanging out with him and get to have lunch with him!",
    picture = "https://f1.media.brightcove.com/8/1857624651001/1857624651001_6024423242001_6024364560001-vs.jpg?pubId=1857624651001&videoId=6024364560001"
    )
    bid_three = Bid(
    profile = profile_three,
    name = "Ticket to NYC",
    start_date = "2019-06-21T03:00Z",
    end_date = "2019-09-23T09:30Z",
    start_amount = "5000",
    description = "10 Days 9 Night in NYC Grand Hotel with SPA every single days and can enjoy the most expensive red wine. Also you will be meeting with the famous Kenny and Dalton Instructor in GA which they will teach you how to do extremely badass HTML/CSS which you will have the chance to earn a job that can earn you 5 million dollar per decade. What are you waiting for, Start bidding!",
    picture = "https://media.architecturaldigest.com/photos/5699802bc6772b7614567435/4:3/w_768/new-york-city-guide.jpg"
    )
    bid_four = Bid(
    profile=profile_four,
    name="Ticket to the Space",
    start_date="2019-03-04T02:20Z",
    end_date="2019-09-20T09:09Z",
    start_amount="30000000",
    description="3days and 2night in the space. If lucky you might have the chance to get back to earth. Really worth your time. You can see many stars and probably one moon? hurry up and start bidding for your chance to go to space.",
    picture="https://cdn.mos.cms.futurecdn.net/LFq3F72EYNqZCoA5Ckw26o.jpg"
    )

    bid_one.save()
    bid_two.save()
    bid_three.save()
    bid_four.save()

    Comments(bid = bid_one, profile = profile_four, body='WORTH WORTH WORTH, Hell yea im going to vegas', rating='6').save()
    Comments(bid = bid_two, profile = profile_two, body='FOr charity I in it', rating='1').save()
    Comments(bid = bid_three, profile = profile_one, body='Please please please', rating='9').save()
    Comments(bid = bid_four, profile = profile_four, body='Is this worth my time or is this wasiting me time!?', rating='4').save()

    Donation(profile = profile_one, donation_amount="500").save()
    Donation(profile = profile_two, donation_amount="250").save()
    Donation(profile = profile_three, donation_amount="100").save()
    Donation(profile = profile_four, donation_amount="50").save()

def delete_all(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')
    Bid = apps.get_model('auction', 'Bid')
    Comments = apps.get_model('auction', 'Comments')
    Donation = apps.get_model('auction', 'Donation')
    Profile.objects.all().delete()
    Bid.objects.all().delete()
    Comments.objects.all().delete()
    User.objects.all().delete()
    Donation.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, delete_all)
    ]

