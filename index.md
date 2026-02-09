---
layout: default
title: Health Companion Super App - UX/UI Case Study
---

# Health Companion Super App
## UX/UI Case Study

**Author:** Sergio Abreo Alvarez
**Date:** February 2025


## Project Overview

A mobile app designed to help individuals with managing their intake of medicaments or to set reminders for their medical appointments. The app is also meant to help users find all related information to their medicaments and medical appointments in one place through their respective events

### Problem Statement

People with chronic conditions often juggle medications, appointments, and doctor communication while trying to live their everyday lives. Forgetfulness, disorganization, and poor coordination can negatively affect their health outcomes.

Our challenge is to design an intuitive mobile app that simplifies health management, improves adherence, and helps users feel in control of their care.

### Goals

- Help users manage medication schedules effectively
- Simplify doctor appointment booking and reminders
- Enable communication with healthcare providers
- Track health progress over time


## 1. User Research

### Research Methods

For this project and article, I conducted a series of interviews with persons that are in the age range of 30 to 60 years old in order to get a wider view on what an application of this nature should be.

For privacy reasons, and because the people that interviewed asked to remain anonymous, I will discuss their opinions and needs as a group and refer to them as "They" on this section of the article.

#### Interviews
The way that the interviews were handled, I the "researcher" for this project and product asked a set of simple questions when it comes to the user interface of the application and the User interactions.

My main questions were the following:

1. How should reminders be set, per event, depending on the nature of the event, or should it be a global setting for all events?
2. How should the events be created? 
3. How many details should the user be required to fill in?
4. What details should be required for each event type?
5. Should the app have extensive setting customization? or should it use the accessibility settings taken from the device?
6. What accessibility accommodations would they like to see in the application?

Across the board participants had a consistent set of answers for each question. 

The needs and wants that I could take away from my interview are the following:

1. Reminders should all have the same behavior and should be set globally and only once.
2. Events should be created through the main page, which would then take the user to another page that is dedicated to the event creation.
3. The user should have a visual selector for the medication or appointment selection field, depending on which event type the user selects the following input fields will be displayed accordingly.
4. The required details are only the essential related to each kind of event.
5. The app should require very little to no setup.
6. The users want the input fields to be easy to understand and to fill up.

#### Secondary Research
In order to get a better picture of the utility and need for an application of this nature I also took the liberty to look up existing studies related to what are the impacts of health companion applications for individuals that need to take medications on the regular.

From what I found based on the following articles:

1. Iribarren S, Akande T, Kamp K, Barry D, Kader Y, Suelzer E
Effectiveness of Mobile Apps to Promote Health and Manage Disease: Systematic Review and Meta-analysis of Randomized Controlled Trials
JMIR Mhealth Uhealth 2021;9(1):e21563
URL: https://mhealth.jmir.org/2021/1/e21563
DOI: 10.2196/21563

2. Yihang Peng, MN, Han Wang, MM, Qin Fang, BS 949560838@qq.com, Liling Xie, BS, Lingzhi Shu, MN, Wenjing Sun, MN, and Qin Liu,
Effectiveness of Mobile Applications on Medication Adherence in Adults with Chronic Diseases: A Systematic Review and Meta-Analysis
Journal of Managed Care & Specialty Pharmacy Volume 26, Number 4
URL: https://www.jmcp.org/doi/10.18553/jmcp.2020.26.4.550
DOI: 10.18553/jmcp.2020.26.4.550

Both of those articles explore the benefits of having a companion app to set reminders for medication. While they both express in their own way the need for further research, they did conclude that there is credible evidence that the use of a companion app such as the one for this mini-project has a meaningful impact on a user's ability to adhere to their medication in the long term.

Through the research that I conducted regarding existing articles on this matter I did come across a few more that for the needs of this article would not necessarily add more relevant information that the above mentioned ones. However I did see a recurring theme where they asked the same question multiple times. What are the features of a companion app that make it so users take their medication regularly at the right time? They would also ask a follow up question along the lines of, what new features could be added to the optimal health companion app?

### Key Research Findings

Following the interviews and secondary research, I have the following key findings that dictate the design of the application:

| Finding | Insight | Design Implication |
|---------|---------|-------------------|
| Global setting for reminders | This is done once at the first use and never changes unless the user wants to | Event creation page has one less field, main feature of the app is automated |
| Dedicated page for event creation | Users want a robust mechanism to add event details| Extra page for the application |
| Key UI elements should be images | UI should be simplified to accommodate users with lower cognitive capabilities | Make use of skeuomorphism |
| No dedicated page for event type | Users want to have all relevant information on the same page | No need for dedicated pages for each event type |

## 2. User Personas

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

### Persona 1: Maria Santos

![Persona 1](assets/images/personas/persona1.jpg)

| Attribute | Details |
|-----------|---------|
| **Age** | 54 |
| **Occupation** | Elementary School Teacher |
| **Health Condition** | Type 2 Diabetes and Hypertension |
| **Tech Comfort** | Low to Moderate: uses her phone mainly for calls, messaging, and basic apps |

**Goals:**
- Keep track of her daily medications (metformin, blood pressure pills) without having to memorize times or doses
- Have a single place to see upcoming doctor appointments so she never misses a check-up
- Spend as little time as possible setting up the app so she can focus on her day

**Motivations:**
- After missing a dose of her blood pressure medication and experiencing dizziness at work, Maria wants a reliable system that keeps her on track
- She values simplicity, she does not want to learn a complicated app; she wants something that "just works" after a quick setup

**Pain Points:**
- She currently relies on handwritten notes and memory to manage her medications, which leads to missed doses especially during busy school days
- Coordinating appointments across multiple specialists (endocrinologist, cardiologist, family doctor) is confusing and she has double-booked in the past
- Apps she has tried before required too much setup and had cluttered interfaces that overwhelmed her

**Quote:** *"I just want something simple that reminds me to take my pills and tells me when my next appointment is, I don't need all the bells and whistles."*

### Persona 2: David Chen

<img src="assets/images/personas/persona2.avif" alt="Persona 2" width="300">

| Attribute | Details |
|-----------|---------|
| **Age** | 37 |
| **Occupation** | Software Project Manager |
| **Health Condition** | Asthma and Generalized Anxiety Disorder |
| **Tech Comfort** | High: comfortable with technology and uses multiple productivity apps daily |

### Persona 3: Chris Redfield

<img src="assets/images/personas/persona3.jpg" alt="Persona 3" width="300">

| Attribute | Details |
|-----------|---------|
| **Age** | 70 |
| **Occupation** | Retired |
| **Health Condition** | Depression |
| **Tech Comfort** | Low: has a basic understanding of how to use a phone |

**Goals:**
- Manage his daily depression medication
- Keep up with his treatment to get better
- Have an easy to understand application

**Motivations:**
- Since his wife died a few months back, Chris has been dealing with depression and struggled to take his medications on a regular basis
- He wants to have a reminder that is hard to miss for his medications and routine appointments with the psychologist

**Pain Points:**
- Due to his depression he has very little motivation to do anything which makes it easy for him to not take his depression medication
- He finds technology hard to use and understand without the help of a younger individual, an intuitive design would allow him to use the application
- He wants to have systematic reminders for all important events related to his medication and appointments in order to overcome his depression

**Quote:** *"Since my wife died, I have struggled with depression. It has been difficult for me to keep up with my medication since most days I don't feel like doing anything and want to stay in bed."*

## 3. User Journey Map

![User Journey Map](assets/images/journey-maps/journey-map.png)

### Journey Stages

#### Stage 1: Awareness
- **Actions:** The user learns about the app through a doctor's recommendation, a family member's suggestion, or an app store search after missing a dose or forgetting an appointment
- **Thoughts:** "I need something to help me stay on top of my medications and appointments, but will this app be easy enough for me to use?"
- **Emotions:** Frustrated with current methods of tracking health tasks, but hopeful that a solution exists
- **Pain Points:** Users like Maria rely on handwritten notes that get lost, David feels overwhelmed juggling multiple productivity tools, and Chris lacks the motivation and tech skills to search for a solution on his own
- **Opportunities:** Clear and simple app store descriptions, accessibility-focused marketing, and a reassuring first impression that signals ease of use

#### Stage 2: Onboarding
- **Actions:** The user downloads the app, opens it for the first time, and is guided through a minimal setup process where they configure their global reminder preferences
- **Thoughts:** "This setup is quick, I only need to set my reminder preferences once and I am ready to go"
- **Emotions:** Relieved that the setup requires very little effort, cautiously optimistic about using the app going forward
- **Pain Points:** Users with low tech comfort like Maria and Chris may hesitate at any screen that feels unfamiliar or asks for too much information upfront, while David may want to ensure the app integrates well with his existing routine
- **Opportunities:** A one-screen onboarding flow with clear visual cues, large input fields, and a brief walkthrough that builds confidence without overwhelming the user

#### Stage 3: Daily Use
- **Actions:** The user receives a reminder notification, opens the app, confirms they took their medication, and occasionally checks upcoming appointments on the main screen
- **Thoughts:** "The reminder went off right on time, let me mark my medication as taken so I can move on with my day"
- **Emotions:** Confident and in control of their health routine, with a sense of accomplishment after confirming each dose
- **Pain Points:** Chris may still struggle with motivation on difficult days and could dismiss a notification without acting on it, Maria may find it hard to respond during busy school hours, and David may need the reminder to cut through the noise of his many other app notifications
- **Opportunities:** Persistent or escalating reminders that are hard to miss, a simple one-tap confirmation to mark a dose as taken, and a clear visual summary on the main screen that reinforces progress

#### Stage 4: Appointment Booking
- **Actions:** The user navigates to the event creation page from the main screen, selects the appointment event type, fills in the essential details using visual selectors, and saves the event
- **Thoughts:** "I can see all my upcoming appointments in one place now, no more double-booking or forgetting which specialist I am seeing next"
- **Emotions:** Organized and reassured that their appointments are tracked, less anxious about managing multiple healthcare providers
- **Pain Points:** Maria has double-booked specialists in the past due to poor coordination, Chris needs the input fields to be straightforward and visually guided so he can complete them independently, and David wants the process to be efficient and not require redundant data entry
- **Opportunities:** Visual selectors and skeuomorphic elements that simplify the input process, automatic conflict detection to prevent double-booking, and a unified calendar view that displays both medication and appointment events together

## 4. Wireframes

### Low-Fidelity Wireframes

#### Home Screen

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Home Screen Wireframe](assets/images/wireframes/home-screen.png)

*Description: [Explain the key elements and their purpose]*


#### Medication Reminder Screen

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Medication Reminder Wireframe](assets/images/wireframes/medication-reminder.png)

*Description: [Explain the key elements and their purpose]*


#### Appointment Scheduling Screen

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Appointment Scheduling Wireframe](assets/images/wireframes/appointment-scheduling.png)

*Description: [Explain the key elements and their purpose]*


#### Additional Screens

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

### Design Iterations

#### Iteration 1

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Iteration 1](assets/images/wireframes/iteration1.png)

*What changed and why:* [Explain the evolution]

#### Iteration 2

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Iteration 2](assets/images/wireframes/iteration2.png)

*What changed and why:* [Explain the evolution]


## 5. Prototype

### Interactive Prototype

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[Embed or link to Figma/Adobe XD prototype]

**Angular prototype repo link:** 

### Key Screens

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

![Final Mockup 1](assets/images/prototypes/final-home.png)
![Final Mockup 2](assets/images/prototypes/final-medication.png)
![Final Mockup 3](assets/images/prototypes/final-appointment.png)

### User Flow

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[ the main user flow demonstrated in the prototype]

1. User opens app → Home screen
2. User taps medication reminder → Medication list
3. User schedules appointment → Calendar view
4. [Continue flow...]


## 6. Usability Testing

### Testing Plan

**Goals:**
- [Test goal 1]
- [Test goal 2]

**Participants:** [Number and characteristics of test users]

**Tasks:**
1. [Task 1 - e.g., "Set a medication reminder for 8 AM daily"]
2. [Task 2 - e.g., "Schedule a doctor appointment for next week"]
3. [Task 3 - e.g., "Find your medication history"]

**Metrics:**
- Task completion rate
- Time on task
- Error rate
- User satisfaction (SUS score)

### Feedback Collection Method

[Describe how you collected feedback - think-aloud protocol, post-task questionnaires, etc.]

### Key Findings & Iterations

| Issue Found | Severity | Solution Implemented |
|-------------|----------|---------------------|
| [Issue 1] | High/Medium/Low | [How you fixed it] |
| [Issue 2] | High/Medium/Low | [How you fixed it] |
| [Issue 3] | High/Medium/Low | [How you fixed it] |

### User Feedback Summary

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

> *"[Direct quote from user testing]"* - Participant 1

> *"[Direct quote from user testing]"* - Participant 2


## 7. Reflection

### What I Learned

[Reflect on how the UX design process helped me identify user needs and improve the product]

### Challenges Encountered

1. **[Challenge 1]:** [How i overcame it]
2. **[Challenge 2]:** [How i overcame it]
3. **[Challenge 3]:** [How i overcame it]

### What I Would Do Differently

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[Insights for future projects]

### Conclusion

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[Final thoughts on the project and the UX/UI design process]


## Appendix

### Research Materials

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

- [Article 1](https://www.jmcp.org/doi/10.18553/jmcp.2020.26.4.550)
- [Article 2](https://mhealth.jmir.org/2021/1/e21563)

### All Wireframe Iterations

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[Additional images if needed]

### Full Usability Test Results

PLACE HOLDER TO TEST LAYOUT OF THE PAGE

[Detailed data if applicable]


*This case study was created as part of SOEN 357 at Concordia University.*
