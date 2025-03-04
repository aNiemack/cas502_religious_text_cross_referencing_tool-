from django.shortcuts import render, HttpResponse
import re
from deep_translator import GoogleTranslator
from difflib import SequenceMatcher as sm


def index(request):
    return render(request, "dashboard/index.html")


def search(request):
    searched = [request.GET.get("text-search-1", "")]

    return HttpResponse(highlight_searched(searched, text))


def translate(request):
    searched = request.GET.get("text-search-1", "")

    words_to_highlight = translate_word(searched, "greek", text_greek)

    return HttpResponse(highlight_searched(words_to_highlight, text_greek))


def highlight_searched(searched, text):
    """Takes two strings 'text', 'searched' and finds all instances of 'searched' in 'text', and adds the html 'mark' element
    around them. Returns the modified text. Ignores case when matching. This allows a user to search for text on a page, and have any matches
    highlighted"""

    if len(searched) > 0 and (searched[0] != "" or len(searched) > 1):
        final_markup = text
        for word in searched:
            final_markup = re.sub(
                re.escape(word),
                lambda m: f"<mark>{m.group(0)}</mark>",
                final_markup,
                flags=re.IGNORECASE,
            )
        return final_markup
    else:
        return text


def translate_word(searched, target, target_text):
    """Takes an english word to translate, a target language, and a text to search through. Translates the searched word
       into the target language and then finds matching instances of that word in the text. Performs a fuzzy search to handle variations."""
    translated = GoogleTranslator(source="auto", target=target).translate(searched)
    target_text = re.sub(r"[^\w\s]", "", target_text)
    target_text = target_text.split(" ")
    target_text = [i for i in target_text if i != ""]

    # Try to get the best possible matches, this is not a good way to do this but it can sort of work.
    best_matches = []
    good_matches = []
    ok_matches = []
    not_great_matches = []
    for word in target_text:
        if sm(None, word, translated).ratio() > 0.8:
            best_matches.append(word)
        elif sm(None, word, translated).ratio() > 0.7:
            good_matches.append(word)
        elif sm(None, word, translated).ratio() > 0.6:
            ok_matches.append(word)
        elif sm(None, word, translated).ratio() > 0.5:
            not_great_matches.append(word)

    if len(best_matches) > 0:
        return list(set(best_matches))
    elif len(good_matches) > 0:
        return list(set(good_matches))
    elif len(ok_matches) > 0:
        return list(set(ok_matches))
    elif len(not_great_matches) > 0:
        return list(set(not_great_matches))
    else:
        return []
    


# Mock loading in the text here just as we would on initial page load
text = """
          Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the east came to Jerusalem,
          saying, "Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him."
          When Herod the king heard this, he was troubled, and all Jerusalem with him;
          and assembling all the chief priests and scribes of the people, he inquired of them where the Christ was to be born.
          They told him, "In Bethlehem of Judea, for so it is written by the prophet:
          "' And you, O Bethlehem, in the land of Judah, are by no means least among the rulers of Judah; for from you shall come a ruler who will shepherd my people Israel.'"
          Then Herod summoned the wise men secretly and ascertained from them what time the star had appeared.
          And he sent them to Bethlehem, saying, "Go and search diligently for the child, and when you have found him, bring me word, that I too may come and worship him."
          After listening to the king, they went on their way. And behold, the star that they had seen when it rose went before them until it came to rest over the place where the child was.
          When they saw the star, they rejoiced exceedingly with great joy.
          And going into the house they saw the child with Mary his mother, and they fell down and worshiped him. Then, opening their treasures, they offered him gifts, gold and frankincense and myrrh.
          And being warned in a dream not to return to Herod, they departed to their own country by another way.
          Now when they had departed, behold, an angel of the Lord appeared to Joseph in a dream and said, "Rise, take the child and his mother, and flee to Egypt, and remain there until I tell you, for Herod is about to search for the child, to destroy him."
          And he rose and took the child and his mother by night and departed to Egypt
          and remained there until the death of Herod. This was to fulfill what the Lord had spoken by the prophet, "Out of Egypt I called my son."
          Then Herod, when he saw that he had been tricked by the wise men, became furious, and he sent and killed all the male children in Bethlehem and in all that region who were two years old or under, according to the time that he had ascertained from the wise men.
          Then was fulfilled what was spoken by the prophet Jeremiah:
          "A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children; she refused to be comforted, because they are no more."
          But when Herod died, behold, an angel of the Lord appeared in a dream to Joseph in Egypt,
          saying, "Rise, take the child and his mother and go to the land of Israel, for those who sought the child's life are dead."
          And he rose and took the child and his mother and went to the land of Israel.
          But when he heard that Archelaus was reigning over Judea in place of his father Herod, he was afraid to go there, and being warned in a dream he withdrew to the district of Galilee.
          And he went and lived in a city called Nazareth, that what was spoken by the prophets might be fulfilled: "He shall be called a Nazarene."""

text_greek = """
            Τοῦ δὲ Ἰησοῦ γεννηθέντος ἐν Βηθλεὲμ τῆς Ἰουδαίας ἐν ἡμέραις Ἡρῴδου τοῦ βασιλέως, ἰδοὺ μάγοι ἀπὸ ἀνατολῶν παρεγένοντο εἰς Ἱεροσόλυμα
            λέγοντες Ποῦ ἐστιν ὁ τεχθεὶς βασιλεὺς τῶν Ἰουδαίων; εἴδομεν γὰρ αὐτοῦ τὸν ἀστέρα ἐν τῇ ἀνατολῇ καὶ ἤλθομεν προσκυνῆσαι αὐτῷ.
            ἀκούσας δὲ ὁ βασιλεὺς Ἡρῴδης ἐταράχθη, καὶ πᾶσα Ἱεροσόλυμα μετ’ αὐτοῦ,
            καὶ συναγαγὼν πάντας τοὺς ἀρχιερεῖς καὶ γραμματεῖς τοῦ λαοῦ ἐπυνθάνετο παρ’ αὐτῶν ποῦ ὁ Χριστὸς γεννᾶται.
            οἱ δὲ εἶπαν αὐτῷ Ἐν Βηθλεὲμ τῆς Ἰουδαίας· οὕτως γὰρ γέγραπται διὰ τοῦ προφήτου·
            Καὶ σὺ Βηθλεέμ, γῆ Ἰούδα, οὐδαμῶς ἐλαχίστη εἶ ἐν τοῖς ἡγεμόσιν Ἰούδα· ἐκ σοῦ γὰρ ἐξελεύσεται ἡγούμενος, ὅστις ποιμανεῖ τὸν λαόν μου τὸν Ἰσραήλ.
            Τότε Ἡρῴδης λάθρᾳ καλέσας τοὺς μάγους ἠκρίβωσεν παρ’ αὐτῶν τὸν χρόνον τοῦ φαινομένου ἀστέρος,
            καὶ πέμψας αὐτοὺς εἰς Βηθλεὲμ εἶπεν Πορευθέντες ἐξετάσατε ἀκριβῶς περὶ τοῦ παιδίου· ἐπὰν δὲ εὕρητε, ἀπαγγείλατέ μοι, ὅπως κἀγὼ ἐλθὼν προσκυνήσω αὐτῷ.
            οἱ δὲ ἀκούσαντες τοῦ βασιλέως ἐπορεύθησαν· καὶ ἰδοὺ ὁ ἀστὴρ, ὃν εἶδον ἐν τῇ ἀνατολῇ, προῆγεν αὐτούς ἕως ἐλθὼν ἐστάθη ἐπάνω οὗ ἦν τὸ παιδίον.
            ἰδόντες δὲ τὸν ἀστέρα ἐχάρησαν χαρὰν μεγάλην σφόδρα.
            καὶ ἐλθόντες εἰς τὴν οἰκίαν εἶδον τὸ παιδίον μετὰ Μαρίας τῆς μητρὸς αὐτοῦ, καὶ πεσόντες προσεκύνησαν αὐτῷ, καὶ ἀνοίξαντες τοὺς θησαυροὺς αὐτῶν προσήνεγκαν αὐτῷ δῶρα, χρυσὸν καὶ λίβανον καὶ σμύρναν.
            καὶ χρηματισθέντες κατ’ ὄναρ μὴ ἀνακάμψαι πρὸς Ἡρῴδην, δι’ ἄλλης ὁδοῦ ἀνεχώρησαν εἰς τὴν χώραν αὐτῶν.
            Ἀναχωρησάντων δὲ αὐτῶν, ἰδοὺ ἄγγελος Κυρίου φαίνεται κατ’ ὄναρ τῷ Ἰωσὴφ λέγων Ἐγερθεὶς παράλαβε τὸ παιδίον καὶ τὴν μητέρα αὐτοῦ καὶ φεῦγε εἰς Αἴγυπτον, καὶ ἴσθι ἐκεῖ ἕως ἂν εἴπω σοι· μέλλει γὰρ Ἡρῴδης ζητεῖν τὸ παιδίον τοῦ ἀπολέσαι αὐτό.
            ὁ δὲ ἐγερθεὶς παρέλαβεν τὸ παιδίον καὶ τὴν μητέρα αὐτοῦ νυκτὸς καὶ ἀνεχώρησεν εἰς Αἴγυπτον,
            καὶ ἦν ἐκεῖ ἕως τῆς τελευτῆς Ἡρῴδου· ἵνα πληρωθῇ τὸ ῥηθὲν ὑπὸ Κυρίου διὰ τοῦ προφήτου λέγοντος Ἐξ Αἰγύπτου ἐκάλεσα τὸν υἱόν μου.
            Τότε Ἡρῴδης ἰδὼν ὅτι ἐνεπαίχθη ὑπὸ τῶν μάγων ἐθυμώθη λίαν, καὶ ἀποστείλας ἀνεῖλεν πάντας τοὺς παῖδας τοὺς ἐν Βηθλεὲμ καὶ ἐν πᾶσι τοῖς ὁρίοις αὐτῆς ἀπὸ διετοῦς καὶ κατωτέρω, κατὰ τὸν χρόνον ὃν ἠκρίβωσεν παρὰ τῶν μάγων.
            τότε ἐπληρώθη τὸ ῥηθὲν διὰ Ἰερεμίου τοῦ προφήτου λέγοντος
            Φωνὴ ἐν Ῥαμὰ ἠκούσθη, κλαυθμὸς καὶ ὀδυρμὸς πολύς· Ῥαχὴλ κλαίουσα τὰ τέκνα αὐτῆς, καὶ οὐκ ἤθελεν παρακληθῆναι ὅτι οὐκ εἰσίν.
            Τελευτήσαντος δὲ τοῦ Ἡρῴδου, ἰδοὺ ἄγγελος Κυρίου φαίνεται κατ’ ὄναρ τῷ Ἰωσὴφ ἐν Αἰγύπτῳ
            λέγων Ἐγερθεὶς παράλαβε τὸ παιδίον καὶ τὴν μητέρα αὐτοῦ καὶ πορεύου εἰς γῆν Ἰσραήλ· τεθνήκασιν γὰρ οἱ ζητοῦντες τὴν ψυχὴν τοῦ παιδίου.
            ὁ δὲ ἐγερθεὶς παρέλαβεν τὸ παιδίον καὶ τὴν μητέρα αὐτοῦ καὶ εἰσῆλθεν εἰς γῆν Ἰσραήλ.
            ἀκούσας δὲ ὅτι Ἀρχέλαος βασιλεύει τῆς Ἰουδαίας ἀντὶ τοῦ πατρὸς αὐτοῦ Ἡρῴδου ἐφοβήθη ἐκεῖ ἀπελθεῖν· χρηματισθεὶς δὲ κατ’ ὄναρ ἀνεχώρησεν εἰς τὰ μέρη τῆς Γαλιλαίας,
            καὶ ἐλθὼν κατῴκησεν εἰς πόλιν λεγομένην Ναζαρέτ· ὅπως πληρωθῇ τὸ ῥηθὲν διὰ τῶν προφητῶν ὅτι Ναζωραῖος κληθήσεται.
        """
