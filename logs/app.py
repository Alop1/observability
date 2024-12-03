import random
from datetime import datetime, timedelta
import os

DEFAULT_LOG_NUM = 2

messages = ["Ludzie, Geralt, lubią wymyślać potwory i potworności. Sami sobie wydają się wtedy mniej potworni. Kiedy rzucą się z widłami na jakiegoś potwora, znajdą kogoś gorszego, poczują się lepsi. Na tym polega ich zadowolenie z życia. Nie, Geralt, ja się ludzi nie boję.",
 "Wiedzminie, każda historia, każda opowieść ma dwie strony. Czasem więcej. Człowiek ma tendencję do oceniania zbyt pochopnie, kierując się tylko jedną z nich. To nigdy nie prowadzi do prawdy.",
 "Kiedy dzieci proszą o bajki, zawsze kończą się one dobrze. Kiedy dorosły pyta o bajkę, wie, że kończy się śmiercią. Rzeczywistość rzadko pozwala na szczęśliwe zakończenia, a bajki są dla tych, którzy chcą zapomnieć.,",
 "Nie ma niczego bardziej ohydnego niż ludzie, którzy wiedzą, że mają rację. Życie nauczyło mnie, że ci, którzy najgłośniej krzyczą o prawdzie i sprawiedliwości, są pierwszymi, którzy je łamią",
"Świat nie jest idealny. Walka o jego lepszą wersję jest jedynym, co możemy zrobić, by nadać sens naszemu istnieniu. Ale pamiętaj, że każdy idealizm ma swoje ciemne strony.",
"Każde zaklęcie, każda magia ma swoją cenę. Nawet jeżeli nie widzisz jej od razu, kiedyś przyjdzie dzień zapłaty. A magia rzadko bywa łaskawa.",
 "Ktoś mi kiedyś powiedział, że przyjaźń to najpiękniejszy dar, jaki można ofiarować. Ale życie nauczyło mnie, że ten dar często bywa narzędziem manipulacji. Tak czy inaczej, jest cennym błogosławieństwem",
 "Czas nie leczy ran. Czas pozwala nam tylko nauczyć się z nimi żyć. Ból zawsze pozostaje, ale człowiek uczy się go ignorować",
 "Nie pytaj, dlaczego los rzuca nas tam, gdzie nas rzuca. Czasem nasze decyzje są tylko iluzją wyboru. Prawdziwa moc kryje się w akceptacji tego, co przynosi życie.",
 "Miłość, powiadają, to najpotężniejsza magia. Może i mają rację. Ale jak każda magia, miłość potrafi zranić bardziej niż jakikolwiek miecz."
 "dsfsdfsdf"]


def generate_logs(num_logs):

    messages = ["Actions started", "Actions stopped", "The car is on the road"]
    users = ["user123", "user456", "user789", "admin", "guest"]
    sessions = ["session1", "session2", "test1", "test2", "session3"]
    log_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]


    log_file_path = "app.log"



    with open(log_file_path, "a") as log_file:
        for _ in range(num_logs):
            random_date = datetime.now() - timedelta(
                days=random.randint(0, 365), seconds=random.randint(0, 86400)
            )
            timestamp = random_date.strftime("[%Y-%m-%d %H:%M:%S]")

            message = random.choice(messages)
            user = random.choice(users)
            session = random.choice(sessions)
            log_level = random.choice(log_levels)

            log_entry = (
                f"{timestamp} [{log_level}] {message} - user_id={user}, session={session}\n"
            )

            log_file.write(log_entry)


if __name__ == "__main__":
    # import argparse
    #
    # # Set up argument parsing
    # parser = argparse.ArgumentParser(description="Generate logs and append to a file.")
    # parser.add_argument("num_logs", type=int, help="Number of logs to generate", default=DEFAULT_LOG_NUM)
    # args = parser.parse_args()

    # Generate the logs
    generate_logs(DEFAULT_LOG_NUM)
