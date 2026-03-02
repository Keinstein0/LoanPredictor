# LoanPredictor
## Teil 1

Als erstes fand ich einen sehr interessanten Datensatz zur verteilung von Darlehen in den USA (https://www.kaggle.com/datasets/miadul/personal-finance-ml-dataset). Ich werde mit diesem arbeiten da er einige spalten hat welche gut miteinander reagieren und man akkurate Vorhersagen treffen könnte.

### Teil 1.1
Für dies lud ich das csv erst einmals herunter. Danach entfernte ich unnötige Spalten so dass nur noch relevante daten in das Modell gefüttert werden. 

### Teil 1.2
Ich entschied mich dafür nur die folgenden Kathegorien beizubehalten sowie alle individuen welche keine schulden haben herauszufiltern. So beinhaltet der Datensatz die nötigen daten anhand derer man den Finanziellen status eines Individuums auslesen kann.

- **age** (alter)
- **gender** (geschlecht)
- **education_level** (studienlevel)
- **employment_status** (anstellung)
- **monthly_income_usd** (einkommen)
- **monthly_expenses_usd** (ausgaben)
- **savings_usd** (erspartes)
- **interest_rate** (output) 

Der Datensatz tangiert die Datenschutzrichtlinien in der tat da er einige Schützenswerte daten beinhaltet (wie Einkommen). Trotzdem ist der Datenschutz gewährt da alle daten sauber vom Ersteller anonymisiert wurden. Es könnte theoretisch möglich sein dass einige der daten auf Individuen zurückverfolgbar wären, jedoch ist durch die entfernung von irrelevanten Daten das Risiko für eine solche Rückverfolgung minimiert worden.