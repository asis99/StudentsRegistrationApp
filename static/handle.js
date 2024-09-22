async function fetchRegCourses() {
    try {
        const response = await fetch('http://localhost:8080/students/courses');
        const courses = await response.json();

        const courseSelect = document.getElementById('rcourse');

        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.course_name;  
            option.text = course.course_name;
            courseSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching courses:', error);
    }
}


async function fetchStudentCourses() {
    try {
        const response = await fetch('http://localhost:8080/students/courses');
        const courses = await response.json();

        const courseSelect = document.getElementById('course');

        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.course_name; 
            option.text = course.course_name;
            courseSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching courses:', error);
    }
}

async function fetchUpdateCourses() {
    try {
        const response = await fetch('http://localhost:8080/students/courses');
        const courses = await response.json();

        const courseSelect = document.getElementById('ucourse');

        
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.course_name;  
            option.text = course.course_name;
            courseSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching courses:', error);
    }
}

async function fetchUpdateStudentCourses() {
    try {
        const response = await fetch('http://localhost:8080/students/courses');
        const courses = await response.json();

       
        const courseSelect = document.getElementById('student-data-course');

       
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.course_name; 
            option.text = course.course_name;
            courseSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching courses:', error);
    }
}

// Call fetchCourses when the page loads
document.addEventListener('DOMContentLoaded', fetchRegCourses);
document.addEventListener('DOMContentLoaded', fetchUpdateStudentCourses);
document.addEventListener('DOMContentLoaded', fetchStudentCourses);
document.addEventListener('DOMContentLoaded', fetchUpdateCourses);

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tabcontent[i].classList.remove("active");
    }

   
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }

    // Show the selected tab and add "active" class to the clicked tab
    document.getElementById(tabName).style.display = "block";
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
}


document.getElementById('studentdeleteform').addEventListener('submit', function(e){
    e.preventDefault();

    const formData = {
        name: document.getElementById('student_name').value,
        dob: document.getElementById('student_dob').value,
        course: document.getElementById('rcourse').value
    };

    console.log(formData)
    fetch('http://localhost:8080/students', {
        method:'DELETE',
        headers:{
            'Content-type':'application/json'
        },
        body:JSON.stringify(formData)
    })
    .then(response=>response.json())
    .then(data=>{
        console.log("Success", data)
        alert("Student Deleted Successfully")
    })
    .catch((error)=>{
        console.log("error is", error)
        alert("Failedailed")
    })

})

document.getElementById('studentForm').addEventListener('submit', function (e) {
    e.preventDefault();  

    const formData = {
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        address: document.getElementById('address').value,
        dob: document.getElementById('dob').value,
        course: document.getElementById('course').value
    };

    fetch('http://localhost:8080/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Registration successful!');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Registration failed!');
        });
});



document.getElementById('addcourse').addEventListener('submit', function (e) {
    e.preventDefault();  
    const formData = {
        course_name: document.getElementById('course_name').value,
        fee: document.getElementById('fees').value,
        course_start: document.getElementById('course_start').value,
        course_end: document.getElementById('course_end').value
    };

    fetch('http://localhost:8080/students/courses', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Course added successfuly');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Failed');
        });
});


document.getElementById('updatecourse').addEventListener('submit', function (e) {
    e.preventDefault();  // Prevent the default form submission behavior

    const formData = {
        course_name: document.getElementById('ucourse').value,
        fee: document.getElementById('ufees').value,
        course_start: document.getElementById('ucourse_start').value,
        course_end: document.getElementById('ucourse_end').value
    };

    fetch('http://localhost:8080/students/courses', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Course updated successfully');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Failed');
        });
});



document.getElementById('updatestudentsdata').addEventListener('submit', function (e) {
    e.preventDefault();  
    const formData = {
        name: document.getElementById('student-name').value,
        course: document.getElementById('student-data-course').value,
        dob: document.getElementById('std-dob').value,
        address: document.getElementById('student-address').value,
        paid_fees: document.getElementById('paid-fees').value
    };
    console.log("ok", formData)
    fetch('http://localhost:8080/students', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Course updated successfully');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Failed');
        });
});


async function fetchData() {
    try {
        // console.log("okkkkkk");
        const response = await fetch('http://localhost:8080/students');
        // console.log("okkkkkk");
        const data = await response.json();
        console.log(data);
        const tableBody = document.getElementById('dataTable').getElementsByTagName('tbody')[0];

        tableBody.innerHTML = '';

        data.forEach(item => {
            
            const row = tableBody.insertRow();

            const nameCell = row.insertCell(0);
            nameCell.textContent = item.name;

            const durationCell = row.insertCell(1);
            durationCell.textContent = item.duration !== null ? item.duration : 'N/A';

            const feeCell = row.insertCell(2);
            feeCell.textContent = item.fee !== null ? item.fee : 'N/A';
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
document.addEventListener('DOMContentLoaded', fetchData);


async function StudentCourseAnalytics() {
    try {
        const response = await fetch('http://localhost:8080/students/courses/analytics');
        const data = await response.json();
        console.log(data);
        const tableBody = document.getElementById('st-cs-analytics').getElementsByTagName('tbody')[0];

        console.log(tableBody)
      
        tableBody.innerHTML = '';

        data.forEach(item => {

            console.log(item)
            
            const row = tableBody.insertRow();
            // Create cells for each data point
            const courseCell = row.insertCell(0);
            courseCell.textContent = item.course;

            const countCell = row.insertCell(1);
            countCell.textContent = item.student_count !== null ? item.student_count : 'N/A';

            const totalfeeCell = row.insertCell(2);
            totalfeeCell.textContent = item.total_fee !== null ? item.total_fee : 'N/A';

        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {

    StudentCourseAnalytics();

    setInterval(StudentCourseAnalytics, 5000);

});



async function UpdateStudentsfetchData() {
    try {
        console.log("okkkkkk");
        const response = await fetch('http://localhost:8080/students');
        console.log("okkkkkk");
        const data = await response.json();
        console.log(data);
        const tableBody = document.getElementById('UpdateStudentdataTable').getElementsByTagName('tbody')[0];

        console.log(tableBody)

        tableBody.innerHTML = '';

        data.forEach(item => {

            console.log(item)
            
            const row = tableBody.insertRow();
            // Create cells for each data point
            const nameCell = row.insertCell(0);
            nameCell.textContent = item.name;

            const dobCell = row.insertCell(1);
            dobCell.textContent = item.dob !== null ? item.dob : 'N/A';

            const feeCell = row.insertCell(2);
            feeCell.textContent = item.fee !== null ? item.fee : 'N/A';

            const paidFeeCell = row.insertCell(3);
            paidFeeCell.textContent = item.paid_fees !== null ? item.paid_fees : 'N/A';

            const pendingFeeCell = row.insertCell(4);
            pendingFeeCell.textContent = item.pending !== null ? item.pending : 'N/A';

            const addressCell = row.insertCell(5);
            addressCell.textContent = item.address !== null ? item.address : 'N/A';
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {

    UpdateStudentsfetchData();

    setInterval(UpdateStudentsfetchData, 5000);
});


