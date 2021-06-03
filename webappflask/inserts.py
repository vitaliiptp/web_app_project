from webappflask import db
from webappflask.models import Recipe, Post, Item
from datetime import datetime


def populate_recipes():
    avocado_toast = Recipe(
        title="Zingy avocado on toast",
        serves="4",
        preptime="15 min",
        description="1. Toast the bread."
                    "2. Peel, stone and mash the avocado flesh with the lemon juice. "
                    "3. Add the Alpro Plain soya alternative to Greek Style yogurt and chilli flakes, season to taste and stir until everything’s well mixed. "
                    "4. Spread the avocado chilli mix on the toast, sprinkled with some extra chilli flakes, if you like it hot! ",
    )
    porridge = Recipe(
        title="Carrot cake porridge",
        serves="4",
        preptime="20 min",
        description="1. Peel and finely grate the carrots. "
                    "2. Pour the Alpro Almond No Sugars drink into a saucepan, add the carrot, raisins, cinnamon and vanilla essence. "
                    "3. Simmer gently on a low heat for 5-10 minutes until the carrots are tender, giving it a stir every now and then. "
                    "4. Stir in the rolled oats and carry on stirring until the porridge starts to thicken up. Take off the heat and add an extra splash of almond drink if you think it needs it. "
                    "5. Divide between your bowls and top with a scatter of nuts. Dig in while deliciously hot! ",
    )
    pancakes = Recipe(
        title="Raspberry, vanilla, coconut and passionfruit pancakes",
        serves="4-6 portions",
        preptime="20 min",
        description="1. Add and mix through the almond milk, coconut oil, vinegar, if using, maple and lemon zest."
                    "2. Heat a non-stick frying- pan over a high heat and if you have one, place a love heart cutter in the pan."
                    "3. Add a little oil to the pan and spoon in about ½ cup of pancake batter. Cook for about 2 minutes then carefully flip and cook for 2 minutes more. If using the heart cutter, remove this before flipping the pancake. Repeat until all the mix has been cooked."
                    "4. To serve, combine the yoghurt with the pulp of 1 passion fruit and spoon this over your pancakes then top with raspberries, coconut maple syrup and more passionfruit. ",
    )

    db.session.add(avocado_toast)
    db.session.add(porridge)
    db.session.add(pancakes)

    db.session.commit()
    db.session.close()


def populate_posts():
    post1 = Post(
        title="HOW ARE ANIMALS HARMED FOR ENTERTAINMENT?",
        date_posted=datetime.utcnow(),
        content="Many of us who love animals want to spent time with them by visiting zoos, aquariums or days at the races. But how ethical are these industries?",
        user_id=1,
    )
    post2 = Post(
        title="WHY SEAFOOD ISN’T A SUPERFOOD",
        date_posted=datetime.utcnow(),
        content="We don’t need to eat fish to be healthy – here’s what to eat instead",
        user_id=1,
    )
    post3 = Post(
        title="VEGAN FISH OPTIONS IN CAFÉS AND RESTAURANTS",
        date_posted=datetime.utcnow(),
        content="Not sure where to find vegan fish alternatives? You’ve come to the right plaice!",
        user_id=1,
    )
    post4 = Post(
        title="FORGOTTEN FISH",
        date_posted=datetime.utcnow(),
        content="Seaspiracy brought home to us just how devastating the fishing industry is for animals, the environment, biodiversity and human rights. It also showed us that fish farms – with their inherent animal suffering and environmental pollution – are not the answer to these problems. Here we share with you some of the most worrying practices and developments in aquatic farming, and talk about the animals who are too often overlooked in discussions about how our dietary choices affect animals and the environment.",
        user_id=1,
    )
    post5 = Post(
        title="TIPS FOR TRANSITIONING FROM VEGGIE TO VEGAN",
        date_posted=datetime.utcnow(),
        content="Need support going from veggie to vegan? We have your back!",
        user_id=1,
    )
    post6 = Post(
        title="EASY VEGAN PASTA RECIPES",
        date_posted=datetime.utcnow(),
        content="Looking for easy pasta vegan pasta recipes that don’t require tons of time and effort? We’ve got you covered!",
        user_id=1,
    )
    post7 = Post(
        title="Vegan Onion Tart with Asparagus",
        date_posted=datetime.utcnow(),
        content="",
        user_id=1,
    )
    post8 = Post(
        title="THE ULTIMATE GUIDE TO KOREAN VEGAN FOOD",
        date_posted=datetime.utcnow(),
        content="With its diverse flavours and unique health benefits, Korean cooking has captured the attention of foodies worldwide. But if we look back at the history of this cuisine, it has largely been developed around plant-based ingredients, with meat and dairy used sparsely or even left out. To celebrate Buddha’s birthday, we’ve put together a comprehensive guide to K-Veganism and why you should try it.",
        user_id=1,
    )
    post9 = Post(
        title="WHERE TO FIND VEGAN CHICKEN ",
        date_posted=datetime.utcnow(),
        content="Looking for cruelty-free chicken alternatives? There are plenty of cluckin’ tasty dishes available in restaurants",
        user_id=1,
    )
    post10 = Post(
        title="Vegan Onion Tart with Asparagus",
        date_posted=datetime.utcnow(),
        content="To me, onion tart is a real, autumnal soul food: I know the classic from southern Germany and always associate it with the winemaking season. I just need to think about it and can already smell the sweet and sour odor of Federweisser. The great thing about onions is that they are regional and always in season. So why not cook a spring interpretation of the classic? For the seasonal touch, green asparagus will join the onions while thyme and dill add a wonderfully fresh aroma to the onion tart.",
        user_id=1,
    )
    post11 = Post(
        title="Vegan Strawberry Tiramisu",
        date_posted=datetime.utcnow(),
        content="It's no secret that I like sweets. In fact, I like it so much that I could eat dessert for breakfast. If there's something sweet left over, don't worry – I will sacrifice myself as I don't want it to go to waste. This is why I was delighted to create a variation of the Italian dessert classic tiramisu that completely suits my tastes – I put all my dessert desired in there (and even opted for a few less sweet components).",
        user_id=1,
    )
    post12 = Post(
        title="Spicy Grilled Tofu Skewers",
        date_posted=datetime.utcnow(),
        content="Barbecue season is right ahead of us! But before I tell you something about our tofu skewers, I have to elaborate on the background story. Last week, after a lot of research, we finally bought a grill for our little office patio. It's not just any grill, though, but one with gas. And even though none of us have had any experience with it before, we were up for the challenge.",
        user_id=1,
    )
    post13 = Post(
        title="Vegan Asparagus Salad à la Salade Niçoise",
        date_posted=datetime.utcnow(),
        content="Well, that was a great task that Julia and Isa have given me: a vegan recipe for Salade Niçoise. I have to admit that I've never eaten this salad before and haven't even heard of it. So the first thing I did was doing some research to find out what goes into it at all. I found the following: the salad originated in France and is also called a Nice Salad, although the first written-down recipe isn't even from Nice, but from Paris. There has probably never been a standard recipe, but a few components apparently can't be missing: tomatoes, olives, anchovies, tuna, potatoes, eggs, and onions. However, since anchovies, tuna, and eggs definitely don't end up on our shopping list, we simply substituted them.",
        user_id=1,
    )
    post14 = Post(
        title="Vegan Chocolate Mousse Cake",
        date_posted=datetime.utcnow(),
        content="Summer is slowly drawing closer and thus also the season of summer cakes – how wonderful! After presenting you a vegan tiramisu cake and a strawberry Swiss roll, here's an option with lots of chocolate! No worries, we're not exaggerating when we promise you lots of chocolate as this cake consists of a moist chocolate cake and a refreshing and fluffy chocolate mousse! You can easily prepare it the day before, so it has enough time to set in the fridge overnight. If you don't have that much time, we'd still recommend to let it chill at least for 3-4 hours.",
        user_id=1,
    )
    post15 = Post(
        title="Vegan Vanilla Waffles with Rhubarb Compote",
        date_posted=datetime.utcnow(),
        content="Maybe you've already discovered it at the market in the last few weeks: rhubarb season is on! From April until the end of June, you still have time to stock up on the spring vegetable and prepare delicious, sweet-sourish desserts with it. Yep, you've read correctly – botanically speaking, rhubarb is actually not a fruit.",
        user_id=1,
    )
    post16 = Post(
        title="Vegan Chicken Marsala Pasta",
        date_posted=datetime.utcnow(),
        content="I've never had Chicken Marsala Pasta before, but the first time I made it myself, I knew right away that it had the potential to be one of my favorite pasta dishes. This may sound cheesy now, but it actually was the case for the entire Zucker&Jagdwurst team. The creamy sauce tastes incredibly slightly sweet and flavorful at the same time thanks to the Marsala wine – we could bathe in it. Together with crispy vegan chicken and pasta, this is definitely a great dish for your cooking routine.",
        user_id=1,
    )
    post17 = Post(
        title="Our Guide to Vegan & Cruelty-Free Clothing",
        date_posted=datetime.utcnow(),
        content="As you could see from the headline, this article has nothing to do with food, but it's a topic that we've often addressed and mentioned in the last article about vegan cosmetics: our clothes. Also, we are no professionals in all areas and thought it's time to take a closer look at this topic. If you approach each area of your everyday life step by step, it's not that difficult and doesn't feel like such a huge change, as if you would suddenly change everything overnight. Promise.",
        user_id=1,
    )
    post18 = Post(
        title="Vegan Buckwheat Galette with Rhubarb",
        date_posted=datetime.utcnow(),
        content="We already have a few galettes on the blog – you may have baked our vegan galette with nectarines, plums and blackberries, with pear and persimmon, and the savory version with tomatoes. They are all baked with shortcrust pastry, but this time everything will be a bit different.",
        user_id=1,
    )

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)
    db.session.add(post17)
    db.session.add(post18)

    db.session.commit()
    db.session.close()


def populate_items():
    item1 = Item(
        name="We Are What We Eat: A Slow Food Manifesto",
        price=22.49,
        author="Alice Waters",
    )
    item2 = Item(
        name="Forks Over Knives―The Cookbook",
        price=3.05,
        author="Del Sroufe",
    )
    item3 = Item(
        name="The Pegan Diet",
        price=12.64,
        author="Dr. Mark Hyman",
    )
    item4 = Item(
        name="Plant Over Processed",
        price=14.90,
        author="Andrea Hannemann",
    )
    item5 = Item(
        name="The Skinnytaste Cookbook",
        price=23.06,
        author="Gina Homolka",
    )
    item6 = Item(
        name="The Plant Paradox Cookbook",
        price=4.41,
        author="Dr. Steven R Gundry",
    )
    item7 = Item(
        name="The Complete Plant-Based Cookbook",
        price=24.96,
        author="America's Test Kitchen",
    )
    item8 = Item(
        name="Ottolenghi Flavor: A Cookbook",
        price=16.00,
        author="Yotam Ottolenghi",
    )
    item9 = Item(
        name="Forks Over Knives: Flavor!",
        price=13.99,
        author="Darshana",
    )
    item10 = Item(
        name="Vegan for Life",
        price=11.56,
        author="Jack Norris",
    )
    item11 = Item(
        name="Six Seasons: A New Way with Vegetables",
        price=15.24,
        author="Joshua McFadden",
    )
    item12 = Item(
        name="Ketotarian",
        price=2.98,
        author="Dr. Will Cole",
    )



    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)
    db.session.add(item11)
    db.session.add(item12)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_recipes()
    populate_posts()
    populate_items()
    print('Successfully populated!')
