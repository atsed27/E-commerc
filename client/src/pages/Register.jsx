import React from 'react';
import { Footer, Navbar } from '../components';
import { Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';

const Register = () => {
  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();
  const submitHandler = async () => {
    console.log('dani');
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
              <label for="Name">Full Name</label>
              <input
                type="email"
                className="form-control"
                id="name"
                placeholder="Enter Your Name"
                {...register('name', {
                  required: 'Please enter your name',
                })}
              />
              {errors.name && (
                <div className="text-danger"> {errors.name.message} </div>
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
