#The Hindu API
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
app=FastAPI()
#facts
facts=[
{
    "fact":"Sanatana Dharma is the original name of Hinduism, meaning 'Eternal Way.'",
    "fact-hindi":"सनातन धर्म हिंदू धर्म का मूल नाम है, जिसका अर्थ है 'शाश्वत मार्ग'।"
},
{
    "fact":"Hinduism is the world's third-largest religion, with over 1.2 billion followers.",
    "fact-hindi":"हिंदू धर्म विश्व का तीसरा सबसे बड़ा धर्म है, जिसके 1.2 अरब से अधिक अनुयायी हैं।"
},
{
    "fact":"It is often called a 'way of life' rather than a structured religion.",
    "fact-hindi":"इसे अक्सर एक संरचित धर्म के बजाय 'जीवन शैली' कहा जाता है।"
},
{
    "fact":"Brahman is the supreme, formless reality that pervades everything.",
    "fact-hindi":"ब्रह्म वह सर्वोच्च, निराकार वास्तविकता है जो हर चीज में व्याप्त है।"
},
{
    "fact":"Atman refers to the individual soul, which is believed to be eternal.",
    "fact-hindi":"आत्मा से तात्पर्य व्यक्तिगत आत्मा से है, जिसे शाश्वत माना जाता है।"
},
{
    "fact":"Karma is the law of action and consequence.",
    "fact-hindi":"कर्म क्रिया और परिणाम का नियम है।"
},
{
    "fact":"Dharma is the moral duty or righteousness one must follow.",
    "fact-hindi":"धर्म वह नैतिक कर्तव्य या धार्मिकता है जिसका पालन करना आवश्यक है।"
},
{
    "fact":"Moksha is the liberation from the cycle of birth and death (Samsara).",
    "fact-hindi":"मोक्ष जन्म और मृत्यु के चक्र (संसार) से मुक्ति है।"
},
{
    "fact":"Samsara is the continuous cycle of reincarnation.",
    "fact-hindi":"संसार पुनर्जन्म का निरंतर चक्र है।"
},
{
    "fact":"Ahimsa is the principle of non-violence toward all living beings.",
    "fact-hindi":"अहिंसा सभी जीवित प्राणियों के प्रति अहिंसा का सिद्धांत है।"
},
{
    "fact":"Artha refers to the pursuit of prosperity and wealth through honest means.",
    "fact-hindi":"अर्थ का तात्पर्य ईमानदारी के माध्यम से समृद्धि और धन की प्राप्ति से है।"
},
{
    "fact":"Purusharthas are the four goals of human life: Dharma, Artha, Kama, and Moksha.",
    "fact-hindi":"पुरुषार्थ मानव जीवन के चार लक्ष्य हैं: धर्म, अर्थ, काम और मोक्ष।"
},
{
    "fact":"Yoga is a group of physical, mental, and spiritual practices originating in India.",
    "fact-hindi":"योग भारत में उत्पन्न शारीरिक, मानसिक और आध्यात्मिक अभ्यासों का एक समूह है।"
},
{
    "fact":"Bhakti is the path of devotion to a personal god.",
    "fact-hindi":"भक्ति व्यक्तिगत ईश्वर के प्रति समर्पण का मार्ग है।"
},
{
    "fact":"Jnana is the path of knowledge and wisdom.",
    "fact-hindi":"ज्ञान, ज्ञान और बुद्धि का मार्ग है।"
},
{
    "fact":"Raja Yoga focuses on meditation and mental control.",
    "fact-hindi":"राज योग ध्यान और मानसिक नियंत्रण पर केंद्रित है।"
},
{
    "fact":"Karma Yoga is the path of selfless action.",
    "fact-hindi":"कर्म योग निस्वार्थ कर्म का मार्ग है।"
},
{
    "fact":"The Aum (Om) symbol represents the primordial sound of the universe.",
    "fact-hindi":"ओम (Aum) प्रतीक ब्रह्मांड की आदिम ध्वनि का प्रतिनिधित्व करता है।"
},
{
    "fact":"The Swastika is a symbol of prosperity and good fortune (dating back thousands of years).",
    "fact-hindi":"स्वास्तिका समृद्धि और सौभाग्य का प्रतीक है (जिसका इतिहास हजारों साल पुराना है)।"
},
{
    "fact":"The Trimurti consists of Brahma, Vishnu, and Shiva.",
    "fact-hindi":"त्रिमूर्ति में ब्रह्मा, विष्णु और शिव शामिल हैं।"
},
{
    "fact":"Brahma is the Creator of the universe.",
    "fact-hindi":"ब्रह्मा ब्रह्मांड के निर्माता हैं।"
},
{
    "fact":"Vishnu is the Preserver and Protector of the universe.",
    "fact-hindi":"विष्णु इस ब्रह्मांड के संरक्षक और रक्षक हैं।"
},
{
    "fact":"Shiva is the Destroyer or Transformer who facilitates rebirth.",
    "fact-hindi":"शिव संहारक या रूपांतरणकर्ता हैं जो पुनर्जन्म को सुगम बनाते हैं।"
},
{
    "fact":"The Tridevi consists of Saraswati, Lakshmi, and Parvati.",
    "fact-hindi":"त्रिदेवी में सरस्वती, लक्ष्मी और पार्वती शामिल हैं।"
},
{
    "fact":"Saraswati is the goddess of knowledge, music, and arts.",
    "fact-hindi":"सरस्वती ज्ञान, संगीत और कला की देवी हैं।"
},
{
    "fact":"Lakshmi is the goddess of wealth, fortune, and prosperity.",
    "fact-hindi":"लक्ष्मी धन, सौभाग्य और समृद्धि की देवी हैं।"
},
{
    "fact":"Parvati is the goddess of power, love, and devotion.",
    "fact-hindi":"पार्वती शक्ति, प्रेम और भक्ति की देवी हैं।"
},
{
    "fact":"Ganesha, the elephant-headed god, is the remover of obstacles.",
    "fact-hindi":"हाथी के सिर वाले देवता गणेश बाधाओं को दूर करने वाले हैं।"
},
{
    "fact":"Hanuman is the monkey-god known for his ultimate devotion to Rama.",
    "fact-hindi":"हनुमान वानर देवता हैं जो राम के प्रति अपनी परम भक्ति के लिए जाने जाते हैं।"
},#To be done
{
    "fact":"Krishna is the 8th avatar of Vishnu and a central figure in the Mahabharata.",
    "fact-hindi":"कृष्ण विष्णु के 8वें अवतार हैं और महाभारत में एक केंद्रीय पात्र हैं।"
},
{
    "fact":"Rama is the 7th avatar of Vishnu and the hero of the Ramayana.",
    "fact-hindi":"राम विष्णु के 7वें अवतार हैं और रामायण के नायक हैं।"
},
{
    "fact":"There are Dashavatara (10 primary avatars) of Lord Vishnu.",
    "fact-hindi":"भगवान विष्णु के दशावतार (10 प्राथमिक अवतार) हैं।"
},
{
    "fact":"Durga is a warrior goddess who represents the victory of good over evil.",
    "fact-hindi":"दुर्गा एक योद्धा देवी हैं जो बुराई पर अच्छाई की जीत का प्रतिनिधित्व करती हैं।"
},
{
    "fact":"Kali is the fierce form of the Divine Mother, representing time and change.",
    "fact-hindi":"काली दिव्य माँ का भयंकर रूप हैं, जो समय और परिवर्तन का प्रतिनिधित्व करती हैं।"
},
{
    "fact":"Murugan (Kartikeya) is the god of war and the son of Shiva and Parvati.",
    "fact-hindi":"मुुरुगन (कार्तिकेय) युद्ध के देवता और शिव और पार्वती के पुत्र हैं।"
},
{
    "fact":"Indra is the king of the Devas and the god of rain and thunder.",
    "fact-hindi":"इंद्र देवों के राजा और वर्षा एवं गरज के देवता हैं।"
},
{
    "fact":"Agni is the god of fire and a messenger between humans and gods.",
    "fact-hindi":"अग्नि अग्नि के देवता हैं और मनुष्यों और देवताओं के बीच एक संदेशवाहक हैं।"
},
{
    "fact":"Surya is the sun god, often depicted in a chariot with seven horses.",
    "fact-hindi":"सूर्य सूर्य देव हैं, जिन्हें अक्सर सात घोड़ों वाले रथ में दिखाया जाता है।"
},
{
    "fact":"Vayu is the god of wind.",
    "fact-hindi":"वायु पवन के देवता हैं।"
},
{
    "fact":"Varuna is the god of the oceans and water.",
    "fact-hindi":"वरुण महासागरों और जल के देवता हैं।"
},
{
    "fact":"Yama is the god of death and justice.",
    "fact-hindi":"यम मृत्यु और न्याय के देवता हैं।"
},
{
    "fact":"Kubera is the treasurer of the gods and god of wealth.",
    "fact-hindi":"कुबेर देवताओं के कोषाध्यक्ष और धन के देवता हैं।"
},
{
    "fact":"Kamadeva is the Hindu god of human love and desire.",
    "fact-hindi":"कामदेव मानवीय प्रेम और इच्छा के हिंदू देवता हैं।"
},
{
    "fact":"Dhanvantari is the physician of the gods and the father of Ayurveda.",
    "fact-hindi":"धन्वंतरि देवताओं के चिकित्सक और आयुर्वेद के जनक हैं।"
},
{
    "fact":"Shesha (Ananta) is the king of all Nagas who supports the universe.",
    "fact-hindi":"शेष (अनंत) सभी नागों के राजा हैं जो ब्रह्मांड का आधार हैं।"
},
{
    "fact":"Garuda is the mount (Vahana) of Lord Vishnu and king of birds.",
    "fact-hindi":"गरुड़ भगवान विष्णु के वाहन और पक्षियों के राजा हैं।"
},
{
    "fact":"Nandi is the bull who serves as the mount of Lord Shiva.",
    "fact-hindi":"नंदी वह बैल है जो भगवान शिव के वाहन के रूप में कार्य करता है।"
},
{
    "fact":"Ganga is the personification of the holy river Ganges.",
    "fact-hindi":"गंगा पवित्र नदी गंगा का मानवीकरण हैं।"
},
{
    "fact":"Shakti is the concept of feminine creative power.",
    "fact-hindi":"शक्ति स्त्री रचनात्मक शक्ति की अवधारणा है।"
},
{
    "fact":"The Vedas are the oldest scriptures, composed in Vedic Sanskrit.",
    "fact-hindi":"वेद सबसे पुराने शास्त्र हैं, जिनकी रचना वैदिक संस्कृत में की गई है।"
},
{
    "fact":"Rig Veda is the oldest of the four Vedas.",
    "fact-hindi":"ऋग्वेद चारों वेदों में सबसे पुराना है।"
},
{
    "fact":"Sama Veda focuses on melodies and chants.",
    "fact-hindi":"सामवेद धुनों और मंत्रों पर केंद्रित है।"
},
{
    "fact":"Yajur Veda contains rituals and sacrificial formulas.",
    "fact-hindi":"यजुर्वेद में अनुष्ठान और यज्ञ सूत्र शामिल हैं।"
},
{
    "fact":"Atharva Veda deals with everyday life, procedures, and charms.",
    "fact-hindi":"अथर्ववेद रोजमर्रा की जिंदगी, प्रक्रियाओं और मंत्रों से संबंधित है।"
},
{
    "fact":"The Upanishads are philosophical texts discussing the nature of reality.",
    "fact-hindi":"उपनिषद दार्शनिक ग्रंथ हैं जो वास्तविकता की प्रकृति पर चर्चा करते हैं।"
},
{
    "fact":"There are 108 principal Upanishads.",
    "fact-hindi":"मुख्य रूप से 108 उपनिषद हैं।"
},
{
    "fact":"The Puranas are vast anthologies of legends and cosmology.",
    "fact-hindi":"पुराण किंवदंतियों और ब्रह्मांड विज्ञान के विशाल संग्रह हैं।"
},
{
    "fact":"There are 18 Maha Puranas (Great Puranas).",
    "fact-hindi":"18 महापुराण हैं।"
},
{
    "fact":"The Mahabharata is the world's longest epic poem.",
    "fact-hindi":"महाभारत विश्व का सबसे लंबा महाकाव्य है।"
},
{
    "fact":"The Ramayana was written by the sage Valmiki.",
    "fact-hindi":"रामायण की रचना ऋषि वाल्मीकि ने की थी।"
},
{
    "fact":"The Bhagavad Gita occurs on the battlefield of Kurukshetra.",
    "fact-hindi":"भगवद गीता का उपदेश कुरुक्षेत्र के युद्ध के मैदान में हुआ था।"
},
{
    "fact":"Shruti means 'that which is heard' (eternal truths like Vedas).",
    "fact-hindi":"श्रुति का अर्थ है 'जो सुना गया' (वेदों जैसे शाश्वत सत्य)।"
},
{
    "fact":"Smriti means 'that which is remembered' (man-made texts like Epics).",
    "fact-hindi":"स्मृति का अर्थ है 'जो याद रखा गया' (महाकाव्यों जैसे मानव-निर्मित ग्रंथ)।"
},
{
    "fact":"The Manusmriti is an ancient legal text and code of conduct.",
    "fact-hindi":"मनुस्मृति एक प्राचीन कानूनी ग्रंथ और आचार संहिता है।"
},
{
    "fact":"The Yoga Sutras of Patanjali are the foundation of classical Yoga.",
    "fact-hindi":"पतंजलि के योग सूत्र शास्त्रीय योग का आधार हैं।"
},
{
    "fact":"The Arthashastra by Chanakya is a treatise on statecraft and economics.",
    "fact-hindi":"चाणक्य द्वारा रचित अर्थशास्त्र शासनकला और अर्थशास्त्र पर एक ग्रंथ है।"
},
{
    "fact":"The Kamasutra is an ancient text on human desire and sexuality.",
    "fact-hindi":"कामसूत्र मानवीय इच्छा और कामुकता पर एक प्राचीन ग्रंथ है।"
},
{
    "fact":"Ramcharitmanas is a 16th-century retelling of the Ramayana in Awadhi.",
    "fact-hindi":"रामचरितमानस 16वीं शताब्दी में अवधी में रामायण का पुनर्कथन है।"
},
{
    "fact":"The Natya Shastra is the foundational text for Indian performing arts.",
    "fact-hindi":"नाट्य शास्त्र भारतीय प्रदर्शन कलाओं का आधारभूत ग्रंथ है।"
},
{
    "fact":"Varanasi (Kashi) is one of the oldest continuously inhabited cities in the world.",
    "fact-hindi":"वाराणसी (काशी) दुनिया के सबसे पुराने निरंतर बसे हुए शहरों में से एक है।"
},
{
    "fact":"The Ganges River is considered the most sacred river in Hinduism.",
    "fact-hindi":"गंगा नदी को हिंदू धर्म में सबसे पवित्र नदी माना जाता है।"
},
{
    "fact":"Kumbh Mela is the largest religious gathering on Earth.",
    "fact-hindi":"कुंभ मेला पृथ्वी पर सबसे बड़ा धार्मिक जमावड़ा है।"
},
{
    "fact":"Char Dham refers to four pilgrimage sites: Badrinath, Dwarka, Puri, and Rameshwaram.",
    "fact-hindi":"चार धाम चार तीर्थ स्थलों को संदर्भित करता है: बद्रीनाथ, द्वारका, पुरी और रामेश्वरम।"
},
{
    "fact":"Ayodhya is the birthplace of Lord Rama.",
    "fact-hindi":"अयोध्या भगवान राम की जन्मस्थली है।"
},
{
    "fact":"Mathura is the birthplace of Lord Krishna.",
    "fact-hindi":"मथुरा भगवान कृष्ण की जन्मस्थली है।"
},
{
    "fact":"Diwali is the festival of lights, celebrating the victory of light over darkness.",
    "fact-hindi":"दीपावली रोशनी का त्योहार है, जो अंधेरे पर प्रकाश की जीत का जश्न मनाता है।"
},
{
    "fact":"Holi is the festival of colors, marking the arrival of spring.",
    "fact-hindi":"होली रंगों का त्योहार है, जो वसंत के आगमन का प्रतीक है।"
},
{
    "fact":"Navratri is a nine-night festival dedicated to the Goddess Durga.",
    "fact-hindi":"नवरात्रि देवी दुर्गा को समर्पित नौ रातों का त्योहार है।"
},
{
    "fact":"Maha Shivratri is the 'Great Night of Shiva.'",
    "fact-hindi":"महाशिवरात्रि 'शिव की महान रात्रि' है।"
},
{
    "fact":"Raksha Bandhan celebrates the bond between brothers and sisters.",
    "fact-hindi":"रक्षाबंधन भाई-बहनों के बीच के बंधन का उत्सव मनाता है।"
},
{
    "fact":"Janmashtami marks the birth of Lord Krishna.",
    "fact-hindi":"जन्माष्टमी भगवान कृष्ण के जन्म का प्रतीक है।"
},
{
    "fact":"Ganesh Chaturthi celebrates the birth of Ganesha.",
    "fact-hindi":"गणेश चतुर्थी गणेश के जन्म का उत्सव मनाती है।"
},
{
    "fact":"Durga Puja is a major festival, especially prominent in West Bengal.",
    "fact-hindi":"दुर्गा पूजा एक प्रमुख त्योहार है, जो विशेष रूप से पश्चिम बंगाल में प्रसिद्ध है।"
},
{
    "fact":"Pongal and Makar Sankranti are harvest festivals.",
    "fact-hindi":"पोंगल और मकर संक्रांति फसल उत्सव हैं।"
},
{
    "fact":"Kailash Mansarovar is considered the earthly abode of Lord Shiva.",
    "fact-hindi":"कैलाश मानसरोवर को भगवान शिव का सांसारिक निवास माना जाता है।"
},
{
    "fact":"Tirupati Balaji is one of the most visited religious shrines in the world.",
    "fact-hindi":"तिरुपति बालाजी दुनिया के सबसे अधिक देखे जाने वाले धार्मिक स्थलों में से एक है।"
},
{
    "fact":"Angkor Wat in Cambodia was originally built as a Hindu temple.",
    "fact-hindi":"कंबोडिया में अंकोरवाट मूल रूप से एक हिंदू मंदिर के रूप में बनाया गया था।"
},
{
    "fact":"Prambanan in Indonesia is the largest Hindu temple site in Southeast Asia.",
    "fact-hindi":"इंडोनेशिया में प्रम्बानन दक्षिण पूर्व एशिया का सबसे बड़ा हिंदू मंदिर स्थल है।"
},
{
    "fact":"The Lotus flower is a sacred symbol of purity and divinity.",
    "fact-hindi":"कमल का फूल पवित्रता और दिव्यता का एक पवित्र प्रतीक है।"
},
{
    "fact":"A Kalpa is a 'day of Brahma,' equaling 4.32 billion years.",
    "fact-hindi":"एक कल्प 'ब्रह्मा का एक दिन' है, जो 4.32 अरब वर्षों के बराबर है।"
},
{
    "fact":"There are four Yugas (Epochs): Satya, Treta, Dvapara, and Kali.",
    "fact-hindi":"चार युग हैं: सत्य, त्रेता, द्वापर और कलि।"
},
{
    "fact":"We are currently living in Kali Yuga, the age of darkness/ignorance.",
    "fact-hindi":"हम वर्तमान में कलियुग में रह रहे हैं, जो अंधकार/अज्ञान का युग है।"
},
{
    "fact":"Ayurveda is the world's oldest system of medicine.",
    "fact-hindi":"आयुर्वेद दुनिया की सबसे पुरानी चिकित्सा प्रणाली है।"
},
{
    "fact":"Sushruta is known as the 'Father of Surgery' in ancient Hindu tradition.",
    "fact-hindi":"सुश्रुत को प्राचीन हिंदू परंपरा में 'सर्जरी का जनक' कहा जाता है।"
},
{
    "fact":"The concept of Zero (Shunya) was pioneered by ancient Indian mathematicians.",
    "fact-hindi":"शून्य (Shunya) की अवधारणा प्राचीन भारतीय गणितज्ञों द्वारा दी गई थी।"
},
{
    "fact":"Vastu Shastra is the traditional Hindu system of architecture.",
    "fact-hindi":"वास्तु शास्त्र वास्तुकला की पारंपरिक हिंदू प्रणाली है।"
},
{
    "fact":"Jyotisha is the traditional Hindu system of astrology/astronomy.",
    "fact-hindi":"ज्योतिष खगोल विज्ञान/ज्योतिष की पारंपरिक हिंदू प्रणाली है।"
},
{
    "fact":"The Decimal System was developed in ancient India.",
    "fact-hindi":"दशमलव प्रणाली का विकास प्राचीन भारत में हुआ था।"
},
{
    "fact":"Ancient Hindu texts correctly described the Earth as a sphere (Bhugola).",
    "fact-hindi":"प्राचीन हिंदू ग्रंथों में पृथ्वी का सटीक वर्णन एक गोले (भूगोल) के रूप में किया गया था।"
},
{
    "fact":"Brahmastra is described as a weapon of immense destructive power.",
    "fact-hindi":"ब्रह्मास्त्र को अपार विनाशकारी शक्ति वाले शस्त्र के रूप में वर्णित किया गया है।"
},
{
    "fact":"Pushpaka Vimana is a legendary flying chariot mentioned in the Ramayana.",
    "fact-hindi":"पुष्पक विमान रामायण में वर्णित एक पौराणिक उड़ने वाला रथ है।"
},
{
    "fact":"The speed of light was remarkably estimated in commentaries on the Rig Veda.",
    "fact-hindi":"ऋग्वेद के भाष्यों में प्रकाश की गति का उल्लेखनीय अनुमान लगाया गया था।"
},
{
    "fact":"Ancient Hindus calculated the age of the Earth to be billions of years.",
    "fact-hindi":"प्राचीन हिंदुओं ने पृथ्वी की आयु अरबों वर्ष होने की गणना की थी।"
},
{
    "fact":"Prana is the vital life force or breath.",
    "fact-hindi":"प्राण महत्वपूर्ण जीवन शक्ति या श्वास है।"
},
{
    "fact":"Chakras are the seven energy centers in the human body.",
    "fact-hindi":"चक्र मानव शरीर के सात ऊर्जा केंद्र हैं।"
},
{
    "fact":"Kundalini is the dormant spiritual energy at the base of the spine.",
    "fact-hindi":"कुंडलिनी रीढ़ के आधार पर सुप्त आध्यात्मिक ऊर्जा है।"
},
{
    "fact":"The Shilpa Shastras are ancient texts on arts and crafts.",
    "fact-hindi":"शिल्प शास्त्र कला और शिल्प पर प्राचीन ग्रंथ हैं।"
},
{
    "fact":"Hindu temples are often built based on sacred geometry (Mandala).",
    "fact-hindi":"हिंदू मंदिर अक्सर पवित्र ज्यामिति (मंडल) के आधार पर बनाए जाते हैं।"
},
{
    "fact":"Sanskrit is considered a highly systematic and scientific language.",
    "fact-hindi":"संस्कृत को एक अत्यधिक व्यवस्थित और वैज्ञानिक भाषा माना जाता है।"
},
{
    "fact":"Ashramas are the four stages of life.",
    "fact-hindi":"आश्रम जीवन के चार चरण हैं।"
},
{
    "fact":"Brahmacharya is the student stage.",
    "fact-hindi":"ब्रह्मचर्य छात्र जीवन की अवस्था है।"
},
{
    "fact":"Grihastha is the householder stage.",
    "fact-hindi":"गृहस्थ गृहस्वामी की अवस्था है।"
},
{
    "fact":"Vanaprastha is the forest-dweller/retirement stage.",
    "fact-hindi":"वानप्रस्थ वन-निवासी/सेवानिवृत्ति की अवस्था है।"
},
{
    "fact":"Sannyasa is the stage of complete renunciation.",
    "fact-hindi":"संन्यास पूर्ण त्याग की अवस्था है।"
},
{
    "fact":"Varna originally referred to professions: Brahmins, Kshatriyas, Vaishyas, and Shudras.",
    "fact-hindi":"वर्ण मूल रूप से व्यवसायों को संदर्भित करता था: ब्राह्मण, क्षत्रिय, वैश्य और शूद्र।"
},
{
    "fact":"Brahmins were traditionally teachers and priests.",
    "fact-hindi":"ब्राह्मण पारंपरिक रूप से शिक्षक और पुजारी थे।"
},
{
    "fact":"Kshatriyas were warriors and rulers.",
    "fact-hindi":"क्षत्रिय योद्धा और शासक थे।"
},
{
    "fact":"Vaishyas were merchants and farmers.",
    "fact-hindi":"वैश्य व्यापारी और किसान थे।"
},
{
    "fact":"Shudras were laborers and service providers.",
    "fact-hindi":"शूद्र श्रमिक और सेवा प्रदाता थे।"
},
{
    "fact":"Gotra refers to a lineage traced back to a common ancestor.",
    "fact-hindi":"गोत्र एक सामान्य पूर्वज से जुड़ी वंशावली को संदर्भित करता है।"
},
{
    "fact":"Gurukul was the ancient Hindu education system.",
    "fact-hindi":"गुरुकुल प्राचीन हिंदू शिक्षा प्रणाली थी।"
},
{
    "fact":"Samskaras are the 16 rites of passage in a person's life.",
    "fact-hindi":"संस्कार व्यक्ति के जीवन के 16 मुख्य संस्कार हैं।"
},
{
    "fact":"Vivaha is the sacred ritual of marriage.",
    "fact-hindi":"विवाह विवाह का पवित्र अनुष्ठान है।"
},
{
    "fact":"Antyesti is the final rite (funeral) performed after death.",
    "fact-hindi":"अंत्येष्टि मृत्यु के बाद किया जाने वाला अंतिम संस्कार है।"
},
{
    "fact":"Namaste means 'I bow to the divine in you.'",
    "fact-hindi":"नमस्ते का अर्थ है 'मैं आपके भीतर की दिव्यता को नमन करता हूँ'।"
},
{
    "fact":"Bindi represents the 'third eye' of spiritual perception.",
    "fact-hindi":"बिंदी आध्यात्मिक धारणा की 'तीसरी आंख' का प्रतिनिधित्व करती है।"
},
{
    "fact":"Vegetarianism is highly encouraged to practice Ahimsa.",
    "fact-hindi":"अहिंसा का पालन करने के लिए शाकाहार को अत्यधिक प्रोत्साहित किया जाता है।"
},
{
    "fact":"The Cow is considered a sacred animal, representing motherhood.",
    "fact-hindi":"गाय को पवित्र पशु माना जाता है, जो मातृत्व का प्रतिनिधित्व करती है।"
},
{
    "fact":"Fast (Vrat) is observed for self-discipline and purification.",
    "fact-hindi":"आत्म-अनुशासन और शुद्धि के लिए उपवास (व्रत) रखा जाता है।"
},
{
    "fact":"Hinduism has no single founder.",
    "fact-hindi":"हिंदू धर्म का कोई एकल संस्थापक नहीं है।"
},
{
    "fact":"The Indus Valley Civilization shows early signs of Hindu practices.",
    "fact-hindi":"सिंधु घाटी सभ्यता हिंदू प्रथाओं के शुरुआती संकेत दिखाती है।"
},
{
    "fact":"Adi Shankara consolidated the doctrine of Advaita Vedanta.",
    "fact-hindi":"आदि शंकराचार्य ने अद्वैत वेदांत के सिद्धांत को समेकित किया।"
},
{
    "fact":"Ramanuja was the chief exponent of Vishishtadvaita.",
    "fact-hindi":"रामानुज विशिष्टाद्वैत के मुख्य प्रतिपादक थे।"
},
{
    "fact":"Madhvacharya founded the Dvaita school of philosophy.",
    "fact-hindi":"माधवाचार्य ने दर्शन के द्वैत स्कूल की स्थापना की।"
},
{
    "fact":"The Bhakti Movement emphasized personal devotion.",
    "fact-hindi":"भक्ति आंदोलन ने व्यक्तिगत भक्ति पर जोर दिया।"
},
{
    "fact":"Swami Vivekananda introduced Hinduism to the Western world in 1893.",
    "fact-hindi":"स्वामी विवेकानंद ने 1893 में पश्चिमी दुनिया को हिंदू धर्म से परिचित कराया।"
},
{
    "fact":"Mahatma Gandhi used the Hindu principle of Satya (Truth) for independence.",
    "fact-hindi":"महात्मा गांधी ने स्वतंत्रता के लिए सत्य के हिंदू सिद्धांत का उपयोग किया।"
},
{
    "fact":"Bali in Indonesia remains a predominantly Hindu island.",
    "fact-hindi":"इंडोनेशिया का बाली आज भी मुख्य रूप से एक हिंदू द्वीप है।"
},
{
    "fact":"Buddhism, Jainism, and Sikhism share roots with Hinduism.",
    "fact-hindi":"बौद्ध, जैन और सिख धर्म की जड़ें हिंदू धर्म से जुड़ी हैं।"
},
{
    "fact":"The Chola Dynasty built massive temples across South Asia.",
    "fact-hindi":"चोल राजवंश ने पूरे दक्षिण एशिया में विशाल मंदिरों का निर्माण कराया।"
},
{
    "fact":"The Vijayanagara Empire was a major protector of Hindu culture.",
    "fact-hindi":"विजयनगर साम्राज्य हिंदू संस्कृति का एक प्रमुख रक्षक था।"
},
{
    "fact":"Sanskrit literature influenced world-renowned thinkers.",
    "fact-hindi":"संस्कृत साहित्य ने विश्व प्रसिद्ध विचारकों को प्रभावित किया।"
},
{
    "fact":"Hatha Yoga is a globally popular form of physical yoga.",
    "fact-hindi":"हठ योग शारीरिक योग का एक वैश्विक स्तर पर लोकप्रिय रूप है।"
},
{
    "fact":"The word 'Juggernaut' comes from 'Jagannath.'",
    "fact-hindi":"'जगरनॉट' शब्द 'जगन्नाथ' से आया है।"
},
{
    "fact":"'Avatar' is a Sanskrit term meaning 'descent.'",
    "fact-hindi":"'अवतार' एक संस्कृत शब्द है जिसका अर्थ है 'अवतरण' या 'नीचे आना'।"
},
{
    "fact":"'Pundit' comes from the Sanskrit word Pandit, meaning a scholar.",
    "fact-hindi":"'पंडित' शब्द संस्कृत के पंडित शब्द से आया है, जिसका अर्थ है विद्वान।"
},
{
    "fact":"The Maurya Empire helped spread the concepts of Dharma.",
    "fact-hindi":"मौर्य साम्राज्य ने धर्म की अवधारणाओं को फैलाने में मदद की।"
},
{
    "fact":"Ahilyabai Holkar rebuilt many prominent Hindu temples.",
    "fact-hindi":"अहिल्याबाई होल्कर ने कई प्रमुख हिंदू मंदिरों का पुनर्निर्माण कराया।"
},
{
    "fact":"Raja Ram Mohan Roy led the Hindu Renaissance in the 19th century.",
    "fact-hindi":"राजा राम मोहन राय ने 19वीं शताब्दी में हिंदू पुनर्जागरण का नेतृत्व किया।"
},
{
    "fact":"Diyas represent the triumph of knowledge over ignorance.",
    "fact-hindi":"दीये अज्ञान पर ज्ञान की विजय का प्रतिनिधित्व करते हैं।"
},
{
    "fact":"Prasad is food offered to a deity and then shared.",
    "fact-hindi":"प्रसाद देवता को अर्पित किया गया भोजन है जिसे बाद में बांटा जाता है।"
},
{
    "fact":"Aarti is a ritual of waving lighted lamps before an idol.",
    "fact-hindi":"आरती मूर्ति के सामने जलते हुए दीपक घुमाने की एक रस्म है।"
},
{
    "fact":"Bhajans are devotional songs.",
    "fact-hindi":"भजन भक्ति गीत हैं।"
},
{
    "fact":"Mantras are sacred utterances with spiritual power.",
    "fact-hindi":"मंत्र आध्यात्मिक शक्ति वाले पवित्र उच्चारण हैं।"
},
{
    "fact":"The Gayatri Mantra is one of the most revered mantras.",
    "fact-hindi":"गायत्री मंत्र सबसे प्रतिष्ठित मंत्रों में से एक है।"
},
{
    "fact":"Tulsi is a sacred plant found in many Hindu homes.",
    "fact-hindi":"तुलसी एक पवित्र पौधा है जो कई हिंदू घरों में पाया जाता है।"
},
{
    "fact":"Peepal Tree is worshipped for its spiritual significance.",
    "fact-hindi":"पीपल के पेड़ की उसके आध्यात्मिक महत्व के लिए पूजा की जाती है।"
},
{
    "fact":"Rudraksha beads are believed to be the tears of Shiva.",
    "fact-hindi":"माना जाता है कि रुद्राक्ष के मोती शिव के आँसू हैं।"
},
{
    "fact":"Pancha Amrita is a mixture of five sacred foods.",
    "fact-hindi":"पंचामृत पांच पवित्र खाद्यों का मिश्रण है।"
},
{
    "fact":"Abhishekam is the ritual pouring of liquids over a deity.",
    "fact-hindi":"अभिषेकम देवता पर तरल पदार्थ चढ़ाने का अनुष्ठान है।"
},
{
    "fact":"Pradakshina is walking around a temple clockwise.",
    "fact-hindi":"प्रदक्षिणा मंदिर के चारों ओर घड़ी की दिशा में घूमना है।"
},
{
    "fact":"Havan is a fire ritual where offerings are made to Agni.",
    "fact-hindi":"हवन एक अग्नि अनुष्ठान है जिसमें अग्नि को आहुति दी जाती है।"
},
{
    "fact":"Sankalpa is a formal vow made before a ritual.",
    "fact-hindi":"संकल्प एक अनुष्ठान से पहले लिया गया औपचारिक व्रत है।"
},
{
    "fact":"Shanti means 'Peace,' often chanted three times.",
    "fact-hindi":"शांति का अर्थ है 'शांति', जिसे अक्सर तीन बार जपा जाता है।"
},
{
    "fact":"Vahana is the animal vehicle associated with each deity.",
    "fact-hindi":"वाहन प्रत्येक देवता से जुड़ा पशु वाहन है।"
},
{
    "fact":"Gopurams are the ornate entrance towers of temples.",
    "fact-hindi":"गोपुरम मंदिरों के अलंकृत प्रवेश द्वार हैं।"
},
{
    "fact":"Vigraha is the term for a consecrated idol.",
    "fact-hindi":"विग्रह एक प्रतिष्ठित मूर्ति के लिए इस्तेमाल किया जाने वाला शब्द है।"
},
{
    "fact":"Darshan means beholding a holy person or deity.",
    "fact-hindi":"दर्शन का अर्थ किसी पवित्र व्यक्ति या देवता को देखना है।"
},
{
    "fact":"Charan Amrit is holy water from the deity's feet.",
    "fact-hindi":"चरणामृत देवता के चरणों का पवित्र जल है।"
},
{
    "fact":"There are 33 categories (Koti) of divine manifestations.",
    "fact-hindi":"दिव्य अभिव्यक्तियों की 33 श्रेणियां (कोटि) हैं।"
},
{
    "fact":"The Badrinath Temple remains closed for six months in winter.",
    "fact-hindi":"बद्रीनाथ मंदिर सर्दियों में छह महीने बंद रहता है।"
},
{
    "fact":"Nepal was the world's only official Hindu state until 2008.",
    "fact-hindi":"नेपाल 2008 तक दुनिया का एकमात्र आधिकारिक हिंदू राष्ट्र था।"
},
{
    "fact":"The Kailasa Temple is carved out of a single solid rock.",
    "fact-hindi":"कैलाश मंदिर एक ही ठोस चट्टान को काटकर बनाया गया है।"
},
{
    "fact":"Hinduism allows for Atheism through certain schools of thought.",
    "fact-hindi":"हिंदू धर्म विचार के कुछ स्कूलों के माध्यम से नास्तिकता की अनुमति देता है।"
},
{
    "fact":"Blue skin in deities represents infinite nature.",
    "fact-hindi":"देवताओं में नीली त्वचा अनंत प्रकृति का प्रतिनिधित्व करती है।"
},
{
    "fact":"Shiva's Third Eye represents wisdom.",
    "fact-hindi":"शिव की तीसरी आंख ज्ञान का प्रतिनिधित्व करती है।"
},
{
    "fact":"Lord Ganesha wrote down the Mahabharata.",
    "fact-hindi":"भगवान गणेश ने महाभारत लिखी थी।"
},
{
    "fact":"Hanuman is believed to be an immortal (Chiranjeevi).",
    "fact-hindi":"माना जाता है कि हनुमान अमर (चिरंजीवी) हैं।"
},
{
    "fact":"The Mahabharata is the longest epic in world literature.",
    "fact-hindi":"महाभारत विश्व साहित्य का सबसे लंबा महाकाव्य है।"
},
{
    "fact":"Ayurveda literally means 'The Science of Life.'",
    "fact-hindi":"आयुर्वेद का शाब्दिक अर्थ है 'जीवन का विज्ञान'।"
},
{
    "fact":"Kalava is a sacred red thread worn on the wrist.",
    "fact-hindi":"कलावा कलाई पर बांधा जाने वाला एक पवित्र लाल धागा है।"
},
{
    "fact":"The Snake around Shiva's neck represents controlled ego.",
    "fact-hindi":"शिव के गले में सांप नियंत्रित अहंकार का प्रतिनिधित्व करता है।"
},
{
    "fact":"Kamadhenu is a divine cow who grants all wishes.",
    "fact-hindi":"कामधेनु एक दिव्य गाय है जो सभी इच्छाएं पूरी करती है।"
},
{
    "fact":"Kalpavriksha is a mythological wish-fulfilling tree.",
    "fact-hindi":"कल्पवृक्ष एक पौराणिक इच्छा पूरी करने वाला पेड़ है।"
},
{
    "fact":"The Saptarishis are the seven great celestial sages.",
    "fact-hindi":"सप्तर्षि सात महान खगोलीय ऋषि हैं।"
},
{
    "fact":"Nyepi is a day of silence observed in Bali.",
    "fact-hindi":"न्येपी बाली में मनाया जाने वाला मौन का दिन है।"
},
{
    "fact":"Bindi color traditionally had specific meanings.",
    "fact-hindi":"पारंपरिक रूप से बिंदी के रंग के विशिष्ट अर्थ होते थे।"
},
{
    "fact":"Saffron represents sacrifice and spiritual purity.",
    "fact-hindi":"केसरिया रंग त्याग और आध्यात्मिक पवित्रता का प्रतिनिधित्व करता है।"
},
{
    "fact":"A Mala typically has 108 beads.",
    "fact-hindi":"एक माला में आमतौर पर 108 मनके होते हैं।"
},
{
    "fact":"Rakshasas are complex beings, not just simple demons.",
    "fact-hindi":"राक्षस जटिल प्राणी हैं, न कि केवल साधारण राक्षस।"
},
{
    "fact":"The Dharma Wheel is a common symbol in Indic faiths.",
    "fact-hindi":"धर्म चक्र भारतीय धर्मों में एक सामान्य प्रतीक है।"
},
{
    "fact":"River Saraswati is a sacred river mentioned in the Vedas.",
    "fact-hindi":"सरस्वती नदी वेदों में वर्णित एक पवित्र नदी है।"
},
{
    "fact":"Tapas refers to the spiritual heat of discipline.",
    "fact-hindi":"तप अनुशासन की आध्यात्मिक ऊर्जा को संदर्भित करता है।"
},
{
    "fact":"Satya (Truth) is considered a supreme virtue.",
    "fact-hindi":"सत्य (Truth) को सर्वोच्च गुण माना जाता है।"
},
{
    "fact":"Ishvara refers to a personal supreme controller.",
    "fact-hindi":"ईश्वर एक व्यक्तिगत सर्वोच्च नियंत्रक को संदर्भित करता है।"
},
{
    "fact":"Jiva is the individual living entity.",
    "fact-hindi":"जीव व्यक्तिगत जीवित इकाई है।"
},
{
    "fact":"Prakriti is the manifest material nature.",
    "fact-hindi":"प्रकृति प्रकट भौतिक स्वभाव है।"
},
{
    "fact":"Purusha is pure cosmic consciousness.",
    "fact-hindi":"पुरुष शुद्ध ब्रह्मांडीय चेतना है।"
},
{
    "fact":"Vasudhaiva Kutumbakam means 'The world is one family.'",
    "fact-hindi":"वसुधैव कुटुम्बकम का अर्थ है 'विश्व एक परिवार है'।"
}
]
@app.get("/api/all")
def all():
    return [{
        "length":199
    },
    {
        "FACTS":facts
    }
    ]
@app.get("/api/random")
def ran(language:str):
    if language=="English"or language=="english":
        return {random.choice(facts)["fact"]}
    elif language=="Hindi"or language=="hindi":
        return {random.choice(facts)["fact-hindi"]}
@app.get("/",response_class=HTMLResponse)
def home():
    return """
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fjalla+One&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<h1>Welcome to The Hindu facts API </h1>
<p>For more info visit the docs </p>
<style>
p{
color:grey;
font-family:"fjalla one"
}
h1{
font-family:"roboto";
}
</style>
"""
