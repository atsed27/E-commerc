import React from 'react';
import { Footer, Navbar } from '../components';
import { Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const navigate = useNavigate();
  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();

  const submitHandler = async ({ email, password, fname, lname }) => {
    console.log(fname, lname, email);
    let first_name = fname;
    let last_name = lname;

    try {
      const res = await axios.post('http://127.0.0.1:8000/api/user/signup', {
        first_name,
        last_name,
        email,
        password,
      });
      console.log(res.data);
      navigate('/login');
    } catch (error) {
      alert('Something Error');
      console.log(error);
    }
  };
  return (
    <>
      <Navbar />
      <div className="container my-3 py-3">
        <h1 className="text-center">Register</h1>
        <hr />
        <div className="row my-4 h-100">
          <form
            onSubmit={handleSubmit(submitHandler)}
            className="col-md-4 col-lg-4 col-sm-8 mx-auto"
          >
            <div className="form my-3">
              <label for="Name">First Name</label>
              <input
                type="text"
                className="form-control"
                id="fname"
                placeholder="Enter Your First Name"
                {...register('fname', {
                  required: 'Please enter your First name',
                })}
              />
              {errors.fname && (
                <div className="text-danger"> {errors.fname.message} </div>
              )}
            </div>
            <div className="form my-3">
              <label for="Name">Last Name</label>
              <input
                type="text"
                className="form-control"
                id="lname"
                placeholder="Enter Your Last Name"
                {...register('lname', {
                  required: 'Please enter your Last name',
                })}
              />
              {errors.lname && (
                <div className="text-danger"> {errors.lname.message} </div>
              )}
            </div>
            <div className="form my-3">
              <label for="Email">Email address</label>
              <input
                type="email"
                className="form-control"
                id="email"
                placeholder="name@example.com"
                {...register('email', {
                  required: 'Please enter your email',
                  pattern: {
                    value: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/i,
                    message: 'Please enter valid email address',
                  },
                })}
              />
              {errors.email && (
                <div className="text-danger"> {errors.email.message} </div>
              )}
            </div>
            <div className="form  my-3">
              <label for="Password">Password</label>
              <input
                type="password"
                className="form-control"
                id="password"
                placeholder="Password"
                {...register('password', {
                  required: 'Please enter your password',
                  minLength: {
                    value: 6,
                    message: 'password more than 5 chars',
                  },
                })}
              />
            </div>
            {errors.password && (
              <div className="text-danger">{errors.password.message}</div>
            )}
            <div className="my-3">
              <p>
                Already has an account?{' '}
                <Link
                  to="/login"
                  className="text-decoration-underline text-info"
                >
                  Login
                </Link>
              </p>
            </div>
            <div className="text-center">
              <button className="my-2 mx-auto btn btn-dark ">Register</button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default Register;
