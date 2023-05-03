# 2095022 # EMAD ABBASI
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        fb_hr = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a {} year-old: {:.1f} bpm".format(age, fb_hr))
    except ValueError as e:
        print("Invalid age.\nCould not calculate heart rate info.")
        print()