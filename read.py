f = open('valid-wordle-words.txt', 'r')
import random

f = list(f)


word_list = []
for i in f:
    i.upper()
    word_list.append(f'{i[0]}{i[1]}{i[2]}{i[3]}{i[4]}')

common_list = [
    "about", "above", "apple", "beach", "bread", "brick", "brown", "chair", "clear", 
    "cloud", "dance", "drink", "earth", "faith", "flame", "fruit", "glass", "grass", 
    "green", "happy", "heart", "horse", "house", "human", "jelly", "knife", "lemon", 
    "light", "might", "money", "music", "never", "night", "ocean", "pearl", "place", 
    "power", "queen", "rainy", "river", "round", "sharp", "sheep", "smile", "small", 
    "sound", "stone", "study", "sunny", "table", "there", "their", "these", "thing", 
    "think", "tiger", "times", "toast", "train", "trust", "under", "uncle", "vivid", 
    "voice", "water", "where", "which", "wheat", "woman", "world", "write", "young", 
    "zebra", "angel", "birth", "chess", "crime", "crown", "daily", "dream", "eagle", 
    "elbow", "empty", "entry", "error", "field", "flock", "forth", "giant", "grape", 
    "grief", "guest", "guide", "honey", "image", "jewel", "juice", "level", "liver", 
    "magic", "metal", "month", "motor", "noble", "north", "olive", "piano", "pilot", 
    "plant", "queen", "robot", "robin", "scale", "sheer", "shell", "short", "silly", 
    "snake", "sport", "stand", "storm", "sword", "table", "thumb", "title", "today", 
    "total", "track", "truck", "twist", "urban", "valve", "visit", "waste", "whale", 
    "wider", "wound", "wrist", "yacht", "yield", "young", "zebra", "zonal", 
    "abuse", "actor", "admit", "adopt", "adult", "alarm", "alter", "anger", "angle", 
    "apple", "apply", "argue", "arena", "argue", "arise", "arrow", "aside", "asset", 
    "audio", "audit", "avoid", "award", "aware", "badge", "baker", "basis", "beach", 
    "beard", "beast", "begin", "being", "bench", "bible", "birth", "black", "blade", 
    "blame", "blank", "blast", "blend", "blind", "block", "blood", "board", "boost", 
    "brain", "brake", "brand", "bread", "break", "brick", "bride", "brief", "bring", 
    "broad", "brown", "brush", "build", "burst", "cable", "cache", "camel", "canal", 
    "candy", "cargo", "carry", "catch", "cause", "cease", "chain", "chair", "chart", 
    "charm", "chase", "cheap", "cheat", "check", "cheek", "cheer", "chest", "chief", 
    "child", "chill", "china", "choir", "chunk", "civil", "claim", "class", "clean", 
    "clear", "clerk", "click", "climb", "clock", "close", "cloth", "cloud", "coach", 
    "coast", "cover", "craft", "cream", "creep", "crime", "crisp", "cross", "crowd", 
    "crown", "cruel", "crush", "cycle", "daily", "dance", "death", "debut", "delay", 
    "depth", "devil", "diary", "dirty", "donor", "doubt", "draft", "drain", "drama", 
    "dream", "dress", "drink", "drive", "drown", "dusty", "eager", "early", "earth", 
    "eight", "elbow", "elite", "empty", "enemy", "enjoy", "entry", "equal", "equip", 
    "error", "essay", "event", "every", "exact", "exist", "extra", "faint", "faith", 
    "false", "fault", "favor", "feast", "fever", "field", "fight", "final", "first", 
    "flash", "flame", "fleet", "floor", "focus", "force", "forth", "forum", "frame", 
    "fraud", "fresh", "front", "fruit", "fully", "funny", "giant", "given", "globe", 
    "glory", "grace", "grade", "grain", "grant", "grape", "graph", "grass", "great", 
    "green", "greet", "grief", "grill", "group", "guard", "guest", "guide", "habit", 
    "happy", "harsh", "heart", "heavy", "honey", "honor", "horse", "hotel", "house", 
    "human", "humor", "ideal", "image", "index", "inner", "input", "issue", "jeans", 
    "jelly", "joint", "judge", "juice", "knife", "label", "labor", "large", "laser", 
    "laugh", "layer", "lease", "least", "leave", "legal", "lemon", "level", "light", 
    "limit", "liver", "lobby", "local", "logic", "loose", "loyal", "lucky", "lunar", 
    "lunch", "magic", "major", "maker", "mango", "march", "match", "mayor", "metal", 
    "might", "minor", "model", "money", "month", "moral", "motor", "mount", "mouse", 
    "mouth", "movie", "music", "naked", "nerve", "never", "night", "noble", "north", 
    "novel", "nurse", "occur", "ocean", "offer", "often", "onion", "opera", "order", 
    "other", "outer", "owner", "paint", "panel", "paper", "party", "pause", "peace", 
    "pearl", "pedal", "piano", "pilot", "place", "plane", "plant", "plate", "point", 
    "pound", "power", "press", "price", "pride", "prime", "print", "prize", "proof", 
    "proud", "prove", "punch", "queen", "quick", "quiet", "quote", "raise", "range", 
    "rapid", "ratio", "reach", "react", "ready", "realm", "relax", "reply", "river", 
    "robot", "rough", "round", "route", "royal", "rural", "saint", "salad", "sauce", 
    "scale", "scary", "scene", "scent", "scope", "score", "sense", "serve", "shade", 
    "shake", "shape", "share", "sharp", "sheep", "sheet", "shift", "shine", "shirt", 
    "shock", "shoot", "short", "sight", "silly", "since", "skill", "sleep", "slice", 
    "slide", "small", "smart", "smile", "smoke", "snake", "solid", "solve", "sound", 
    "south", "space", "spare", "speak", "speed", "spell", "spend", "spice", "spill", 
    "spine", "split", "spoil", "sport", "spray", "squad", "stack", "staff", "stage", 
    "stair", "stake", "stamp", "stand", "stare", "start", "state", "steak", "steal", 
    "steel", "stick", "still", "stock", "stone", "store", "storm", "story", "strip", 
    "style", "sugar", "sunny", "super", "sword", "table", "taste", "teach", "thank", 
    "theme", "there", "thick", "thing", "think", "third", "those", "throw", "thumb", 
    "tiger", "tight", "tired", "title", "toast", "today", "tooth", "topic", "total", 
    "touch", "tough", "tower", "toxic", "trace", "track", "trade", "trail", "train", 
    "trend", "trial", "tribe", "trick", "troop", "truck", "truly", "trust", "truth", 
    "twice", "twist", "uncle", "under", "union", "unity", "urban", "urine", "usual", 
    "valid", "value", "vapor", "vault", "venue", "video", "vivid", "voice", "waste", 
    "watch", "water", "wheel", "where", "which", "while", "white", "whole", "whose", 
    "woman", "women", "world", "worry", "wound", "wrist", "write", "wrong", "yacht", 
    "yield", "young", "youth", "zebra", "zonal"
]

new_list = []
for i in common_list:
    new_list.append(i.lower())



def string(x):
    y = ''
    for i in x:
        y += i
    return y


