# fagelsang

[_The Birds_](https://en.wikipedia.org/wiki/The_Birds_(play)), translated for birds.

Created for [NaNoGenMo 2021](https://github.com/NaNoGenMo/2021). [Read the entire play](https://github.com/nmifsud/fagelsang/blob/master/fagelsang-211118-141803.pdf) (52,076 words).

Fågelsång is Swedish for "birdsong". I learned it from a peculiar record called [_Nära Naturen_](https://www.discogs.com/master/1216933-Jan-Lindblad-N%C3%A4ra-Naturen) (1977) by [Jan Lindblad](https://en.wikipedia.org/wiki/Jan_Lindblad). Lindblad had a talent for imitating birds by whistling, most impressively on "[Morgonvandring med Fågelsång](https://www.youtube.com/watch?v=cDBNnMakpcg)" ("Morning Walk with Birdsong").

My thinking for this project really started when I read about "[warblish](https://doi.org/10.2993/0278-0771-36.4.765)", which is the imitation of bird sounds using existing language. A classic is the barred owl's *who cooks for you? who cooks for you-all?* Some birders know dozens of these mnemonics. When you spend enough time alone in the woods, the mind runs amok.

The other way to mimic bird sounds with language is onomatopoeia. This is what you find in field guides to help with identification. And in some places birds are named by their calls. For instance, the An̲angu of central Australia know the little crow as Kaanka and the galah as Piyar-piyarpa.

My first attempt to create a birdsong-inspired work involved crafting GPT-3 prompts to translate random onomatopoeic strings into warblish. But the hit rate was abysmal, and I realised that even if it was 100% accurate, the resulting book would be utter nonsense. Nonsense in generative novels is par for the course, but it wouldn't be interesting nonsense. I decided to focus on onomatopoeia, which is fun to read and say out loud. [Aristophanes understood this!](https://youtu.be/P16muiYePu0?t=2790)

I prepped a [Gutenberg version](https://www.gutenberg.org/cache/epub/3013/pg3013.txt) of _The Birds_ by deleting metadata, footnotes and line breaks. The program then splits words into syllables, randomly lengthens vowels, repeats syllables and lines, and appends new sound endings. There's no universal method of transcribing bird sounds. Capturing pitch and rhythm is what really matters, so I didn't try to achieve a consistent orthography. By keeping vowels, pitch is mostly preserved; by keeping opening letters and punctuation, we retain some meaning. The repetitions introduce a more avian cadence. The sound lists in my program were loosely derived from the lexicons of my [Morcombe & Stewart](https://apps.apple.com/au/app/morcombe-stewart-guide/id397979505) field guide and [_Aaaaw to Zzzzzd_](https://mitpress.mit.edu/books/aaaaw-zzzzzd-words-birds) by John Bevis.

`py fagelsang.py` translates the whole play and produces a TeX file. `py fagelsang.py 302` turns
> PISTHETAERUS From whom? Why, from themselves. Don't you know the cawing crow lives five times as long as a man?

into something like this:
> PISTHETAERUS Frooi whoooo whooooo? Whaaark, froee thenk seek vee. Doee nt-nt yoooowk-uhii uhi-knoooop knop thet cak wiah-crok lioo vee-fiee veeeee tit tiiiit tiit mee as-looo aasas-a maai mai?

A far cry from real birdsong, I admit. But worth a laugh. Whaaak whak whak-doee yooowk-yoowk uri thioo?