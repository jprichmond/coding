

fs = require('fs')


const info = {
  name:`Jason Richmond`,
  email:`jason@richmond.is`,
  site:`jason.richmond.is`,
  phone:`574.855.6954`,
  text: [
    `Software Engineer with a Master’s in Computer Science familiar with a diverse array of languages and platforms and a love for teaching seeking a return to the art of cultivating programming knowledge in the next generation`,
  ]
}
const ed = {
  name: `Academic Experience`,
  grad: {
    school:`Indiana University South Bend`,
    gpa:3.7,
    degree:`Master of Science`,
    year:`2021`,
    major:`Computer Science`,
    text: [
      `Studied a wide spectrum in the discipline, from artificial intelligence to algorithm analysis, networking to neural networks, graphics to games, even writing the opcodes for a simulated CPU to run a puck-like robot with enough AI to navigate a maze`
    ]
  },
  undergrad: {
    degree:`Bachelor of Arts`,
    school:`Indiana University Bloomington`,
    year:`2008`,
    gpa: 3.1,
    major: {
      anth:`Anthropology`,
      econ:`Economics`,
      ling:`Linguistics`
    }
  }
}
const work = {
  name: `Experience`,
  aun: {
    name:`Aunalytics`,
    role:`Software Engineer`,
    start:2021,
    end:2023,
    text: [
      `Maintained the microservices and REST API of our data solutions platform written in Node using MongoDB, GraphQL, Hadoop, and Apache Pig`,
      `Achieved subject matter expert in Formations, our in-house data portability framework`,
      `Contributed to initiatives in improve the robustness and fault-tolerance of our data pipeline`,
      `Committed features that sped up our data delivery by an order of magnitude allowing us to achieve our on-time delivery goal of 75 consecutive days`,
      `Took the reins on implementing two-phase procedure for data manipulation so that only valid results would be written to the destination`,
      `Investigated and coded dynamic solution to a logging failure impacting our deliverables`,
      `Pushed for and piloted new team structure to better communicate and increase collaboration`,
      `Engaged in designing our next generation platform written in Typescript using React`
    ]
  },
  sbcs: {
    name:`South Bend Code School`,
    role:`Lead Instructor`,
    start:2018,
    end:2020,
    text: [
      `Crafted interactive learning path spanning eleven lessons of around 25k words in p5, giving students an introduction to procedural, object-oriented, and functional programming paradigms`,
      `Laid a concrete foundation for primary and secondary school students to build out abstract programming concepts using Scratch, HTML, CSS, JavaScript, C#, and Python`,
      `Entrusted with running the Elkhart branch and being liaison to local schools keeping relevant stakeholders happy and extending Code School reach`
    ]
  },
  ace: {
    name:`Academic Center for Excellence`,
    start:2016,
    end:2019,
    role:`Learning Facilitator`,
    sub:`Computer Science`,
    text: [
      `Equipped dozens of graduates and undergraduates of all levels having trouble grokking the theory and practice of Computer Science with the knowledge and skills to succeed`,
      `Debugged hundreds of student-written programs, usually on a tight deadline before submission without reference to a working answer`,
      `Collaborated with professors to help compress the complex world of code into the tangible everyday for entry-level students`]
  }
}

const craft = {
  name: `Development Skills`,
  dev: {
    lang: {
      title: `Languages`,
      names: [
        `Javascript`,
        `Typescript`,
        `HTML/CSS`,
        `Python`,
        `Rust`,
        `Go`,
        `Swift`,
        `C`,
        `C++`,
        `C#`,
        `Java`,
        `SQL`,
        `Assembly`,
        `Supercollider`,
        `CSound`,
      ]
    },
    meth: {
      title: `Methodologies`,
      names: [
        `CI/CD`,
        `TDD`,
        `Agile`,
        `Scrum`,
        `Kanban`,
      ]
    },
    tool: {
      title: `Tools`,
      names: [
        `Node`,
        `React`,
        `Vue`,
        `Storybook`,
        `p5`,
        `Okta`,
        `GraphQL`,
        `MongoDB`,
        `PostgreSQL`,
        `Git`,
        `Docker`,
        `Mocha`,
        `Hadoop`,
        `Apache Pig`,
        `Exasol`,
        `Alluxio`,
        `Jira`,
        `GPTs`,
      ]
    },
    doms: {
      title: `Domains`,
      names: [
        `UI/UX Design`,
        `Full-stack Development`,
        `Microservices`,
        `REST`,
        `Machine Learning`,
        `Neural Networks`,
        `AI`,
      ]
    },
  }
}


out = [info,ed,work,craft]
out = JSON.stringify(out)

const err = new Error('failed to write to file')
fs.writeFile('data.json', out, (e) => e ? console.log(err) :7)