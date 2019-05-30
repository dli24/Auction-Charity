from django.db import migrations
from django.contrib.auth.models import User

def seed(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')
    Bid = apps.get_model('auction', 'Bid')
    Comments = apps.get_model('auction', 'Comments')
    Donation = apps.get_model('auction', 'Donation')

    user1 = User(username='bob', password='testing1234', email='b@b.com', first_name='Bob', last_name='Belcher')
    user1.save()
    user2 = User(username='tom', password='testing1234', email='t@t.com', first_name='Tom', last_name='Hannigan')
    user2.save()
    user3 = User(username='chris', password='testing1234', email='c@c.com', first_name='Chris', last_name='Hemsworth')
    user3.save()
    user4 = User(username='dora', password='testing1234', email='d@d.com', first_name='Dora', last_name='Explorer')
    user4.save()

    profile_one = Profile(user_id=user1.id, bio="Robert 'Bob' Belcher Jr. is a third-generation restaurateur. Bob runs Bob's Burgers with the help of his wife, Linda Belcher, and their three kids, Tina Belcher, Louise Belcher, and Gene Belcher. While poor with business management and cursed with an unlucky streak, his experience and skill in homemade cuisine has helped his restaurant stay afloat, in spite of seemingly constant financial uncertainty, providing for his family all the while.", picture='https://vignette.wikia.nocookie.net/bobsburgerpedia/images/9/95/Bobs-Burgers-Wiki_Archer_Bob_01a.png/revision/latest?cb=20160712225426')
    profile_two = Profile(user_id=user2.id, bio="Willow Danielle Rosenberg was a witch native to Sunnydale, California, founding member of the Scooby Gang, and the best friend and semi-official sidekick of the Slayer, Buffy Summers. Willow started out as a shy computer nerd, eventually developing her talents to become a powerful and assertive witch. Willow was introduced to the forces of magic by attempting a complex spell to re-ensoul Angel. To her own surprise, Willow tapped into considerable power during this ritual, and would come to practice witchcraft. Willow was quick to grasp basic spells and with support from her girlfriend Tara Maclay, her powers blossomed even more rapidly as did her self-confidence. Milestones in her magical career include the enjoining spell, taking on the Hell-Goddess Glory and surviving, resurrecting Buffy Summers, nearly ending the world, activating the world’s Potential Slayers and eventually, establishing herself as Earth’s most powerful witch.", picture='https://vignette.wikia.nocookie.net/buffy/images/6/62/Willow_tk.jpg/revision/latest/scale-to-width-down/1000?cb=20100319183627')
    profile_three = Profile(user_id=user3.id, bio="Chris Hemsworth was born in Melbourne, Australia, to Leonie (van Os), a teacher of English, and Craig Hemsworth, a social-services counselor. His brothers are actors Liam Hemsworth and Luke Hemsworth. He is of Dutch (from his immigrant maternal grandfather), Irish, English, Scottish, and German ancestry. His uncle, by marriage, was Rod Ansell, the bushman who inspired the film Crocodile Dundee (1986).", picture='https://m.media-amazon.com/images/M/MV5BMTYwMTUwNTAyOV5BMl5BanBnXkFtZTgwMTk1OTU5NzM@._V1_SX1777_CR0,0,1777,937_AL_.jpg')
    profile_four = Profile(user_id=user4.id, bio='HI bio four', picture='http://cdn.onlinewebfonts.com/svg/download_525162.png')

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
