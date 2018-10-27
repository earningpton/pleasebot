from slowclap import (MicrophoneFeed, AmplitudeDetector,
                      RateLimitedDetector, VerboseFeed, Detector)

THRESHOLD = 7800000


class MultiClapDetector(Detector):

    def __init__(self, d, rate_limit=1, num_of_claps=2):
        self.child = d
        self.last_clap = -rate_limit
        self.rate_limit = rate_limit
        self.num_of_claps = num_of_claps
        self.claps_per_rate = []

    def __iter__(self):
        for clap in self.child:
            if clap.time - self.last_clap > self.rate_limit:
                self.last_clap = clap.time
                self.claps_per_rate = []
            else:
                self.claps_per_rate.append(clap.time)
                if len(self.claps_per_rate) == self.num_of_claps:
                    yield clap


def detect_one_clap():
    feed = MicrophoneFeed()

    detector = AmplitudeDetector(feed, THRESHOLD)
    detector = RateLimitedDetector(detector, 1)

    for clap in detector:
        return("One Clap")


def detect_two_claps():
    feed = MicrophoneFeed()

    detector = AmplitudeDetector(feed, THRESHOLD)
    detector = MultiClapDetector(detector)
    print(detector.last_clap)

    for clap in detector:
        print("Two Claps")


def main():
    in_put = input("Enter 1/2 for one to two claps:")

    if (input == 1):
        detect_one_clap()
    elif (input == 2):
        detect_two_claps()

